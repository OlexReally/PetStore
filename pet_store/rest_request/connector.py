"""
Wrapper for request module
"""
from pet_store.rest_request.request import *


class Connector:
    """
    Implements static methods for wep-api requests
    """

    @staticmethod
    def get(url, headers):
        """
        Wrapper for get request

        :param url: URL for request
        :param headers: headers for request
        :return: answer from server
        """
        answer = get(url, headers)

        if answer.status_code == 200:
            return answer
        elif answer.status_code == 400:
            raise RuntimeError('Invalid ID supplied')
        elif answer.status_code == 404:
            raise RuntimeError('Requested data not found')

    @staticmethod
    def post(url, data_xml, headers):
        """
        Wrapper for post request

        :param url: URL for request
        :param data_xml: data for request
        :param headers: headers for request
        :return: answer from server
        """
        answer = post(url, data_xml, headers)

        if answer.status_code == 200:
            return answer
        elif answer.status_code == 405:
            raise RuntimeError('Invalid input')
        elif answer.status_code == 400:
            raise RuntimeError('Bad Request')
        elif answer.status_code == 404:
            raise RuntimeError('Requested data not found')

    @staticmethod
    def delete(url, headers):
        """
        Wrapper for post request

        :param url: URL for request
        :param headers: headers for request
        :return: answer from server
        """
        answer = delete(url, headers)

        if answer.status_code == 200:
            return answer
        elif answer.status_code == 400:
            raise RuntimeError('Invalid ID supplied')
        elif answer.status_code == 404:
            raise RuntimeError('Requested data not found')
