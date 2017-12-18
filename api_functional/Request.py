import requests


def getapi(url, headerskeys):
    headers = {headerskeys[0]: headerskeys[1]}
    return requests.get(url, headers=headers)


