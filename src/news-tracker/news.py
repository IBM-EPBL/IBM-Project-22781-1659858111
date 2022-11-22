import requests
from pprint import pprint
from .config import RAPID_API_KEY, API_URI
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import functools



class FreeNews:
    """
    FreeNews RapidAPI Wrapper Class

    """
    def __init__(self):
        self.__header = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "free-news.p.rapidapi.com"
        }
        self.__uri = API_URI


    def __request(self, querystring: dict):
        try:
            req = requests.request("GET", self.__uri, headers=self.__header, params=querystring)
            return req
        except requests.exceptions.RequestException as e:
            return e


    def Search(self, query: str, lang="en"):
        """
        Search for a query which will return a JSON Object

        Arguments:
            query: A string that you want to search

        Returns:
            A JSON object
        """
        query = {
            "q": query,
            "lang": lang,
        }
        res = self.__request(query)
        return res.json()


news = FreeNews()
bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/<query>', methods=['GET', 'POST'])
def news_fetch(query):

    if request.method == 'POST':
        q = request.form['search']
        return redirect(url_for('news.news_fetch', query=q))
    else:
        json_obj = news.Search(str(query))
        if len(json_obj) < 3:
            return render_template('news.html', raw_obj_len=len(json_obj), query=query)
        else:
            return render_template('news.html', query=query, obj=json_obj["articles"], res = len(json_obj["articles"]), raw_obj_len=len(json_obj))


@bp.route('/<query>/JSON')
def news_fetch_json(query):
    json_obj = news.Search(query)
    return json_obj