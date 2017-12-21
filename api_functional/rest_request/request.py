import requests


def get(url, headers):
    return requests.get(url=url, headers=headers)


def post(url, data_xml, headers):
    return requests.post(url=url, data=data_xml, headers=headers)


def delete(url, headers):
    return requests.delete(url=url, headers=headers)


# TODO implement put request
def put(url, headers):
    pass
