"""
    Contains method, which use HTTP request's
"""
import requests


def get(url, headers):
    """
    Wrapper post get request.

    :param url: host URL
    :param headers: headers for request
    :return: answer of get request
    """
    return requests.get(url=url, headers=headers)


def post(url, data_xml, headers):
    """
    Wrapper for post request.

    :param url: host URL
    :param data_xml: xml with necessary changes
    :param headers: headers for request
    :return: answer of post request
    """
    return requests.post(url=url, data=data_xml, headers=headers)


def delete(url, headers):
    """
    Wrapper for delete request.

    :param url: host URL
    :param headers: headers for request
    :return: answer of delete request
    """
    return requests.delete(url=url, headers=headers)


