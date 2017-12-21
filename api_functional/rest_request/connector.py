from api_functional.rest_request.request import *


class Connector:

    @staticmethod
    def get(url, headers):
        answer = get(url, headers)

        if answer.status_code == 200:
            return answer
        elif answer.status_code == 400:
            raise RuntimeError('Invalid ID supplied')
        elif answer.status_code == 404:
            raise RuntimeError('Requested data not found')

    @staticmethod
    def post(url, data_xml, headers):
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
        answer = delete(url, headers)

        if answer.status_code == 200:
            return answer
        elif answer.status_code == 400:
            raise RuntimeError('Invalid ID supplied')
        elif answer.status_code == 404:
            raise RuntimeError('Requested data not found')

    # TODO implement put request
    @staticmethod
    def put(url, headers):
        pass
