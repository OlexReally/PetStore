import requests


def getapi(url, headerskeys):
    headers = {headerskeys[0]: headerskeys[1]}
    print(headers)
    return requests.get(url, headers=headers)


