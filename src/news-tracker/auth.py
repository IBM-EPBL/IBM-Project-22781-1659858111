from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import functools
from .db import create_conn
import ibm_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #print(f"{username} and {password}")

        db = create_conn()

        error = None    

        if error is None:
            try:
                sql = "SELECT * FROM USER WHERE USERNAME =?"
                stmt = ibm_db.prepare(db, sql)
                ibm_db.bind_param(stmt,1,username)
                ibm_db.execute(stmt)
                acc = ibm_db.fetch_both(stmt)
                if username == acc[1]:
                    print("User with the username already exists! Please try another username.")
                    return redirect(url_for('auth.register'))
            except:
                insert_sql = "INSERT INTO USER(USERNAME, PASSWD) VALUES (?,?)"
                prep_stmt = ibm_db.prepare(db, insert_sql)
                ibm_db.bind_param(prep_stmt, 1, username)
                ibm_db.bind_param(prep_stmt, 2, generate_password_hash(password, salt_length=69))
                ibm_db.execute(prep_stmt)
                print("Successfule registration!")
                return redirect(url_for('auth.login'))
    else:

        return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(f"{username} and {password}")
        
        db = create_conn()
        error = None

        try:
            sql = "SELECT * FROM user WHERE username =?"
            stmt = ibm_db.prepare(db, sql)
            ibm_db.bind_param(stmt,1,username)
            ibm_db.execute(stmt)
            user = ibm_db.fetch_both(stmt)

            res = check_password_hash(user[2], password)

            #print("Both are ", "correct" if res is True else "wrong")

            
            if res is False:
                error = "Password or username is incorrect!"
                print("Password or username is incorrect!")
                return redirect(url_for('auth.login'))
            else:
                session.clear()
                session['user_id'] = user[0]
                print("Login Successful")
                return redirect(url_for('index'))
                
            
        except Exception as e:
            print("Some error :( : ", e)
            return render_template('auth/login.html')
        
    else:
        return render_template('auth/login.html')


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = create_conn()
        sql = "SELECT * FROM USER WHERE ID =?"
        stmt = ibm_db.prepare(db, sql)
        ibm_db.bind_param(stmt,1,user_id)
        ibm_db.execute(stmt)
        user = ibm_db.fetch_both(stmt)
        g.user = user
       