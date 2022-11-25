import ibm_db
from .config import DB_URL
#from werkzeug.security import check_password_hash, generate_password_hash

def create_conn():
    try:
        conn = ibm_db.connect(DB_URL, '', '')
        return conn
    except:
        print("Error establishing connection : ", ibm_db.conn_errormsg())



