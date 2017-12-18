import requests


def getapi(url):
    return requests.get(url, headers={'accept': 'application/xml'})


