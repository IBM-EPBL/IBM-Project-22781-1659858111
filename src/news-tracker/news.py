import requests
from pprint import pprint
from config import RAPID_API_KEY, API_URI


class FreeNews:
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
        query = {
            "q": query,
            "lang": lang,
        }
        res = self.__request(query)
        return res.json()


g = FreeNews()
print(pprint(g.Search("russia")))
