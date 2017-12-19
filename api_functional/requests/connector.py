from api_functional.requests.request import *


class Connector:
    # __URL = "http://petstore.swagger.io/v2/pet/"
    # __HEADERS = {'accept': 'application/xml'}
    # __URL = "http://petstore.swagger.io/v2/"
    # __HEADERS = {'accept': 'application/xml'}
    # __PET = "pet/"

    @staticmethod
    def get(url, headers={'accept': 'application/xml'}):
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
