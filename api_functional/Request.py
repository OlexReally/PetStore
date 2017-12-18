import requests


def getapi(url):
    answer = requests.get(url, headers={'accept': 'application/xml'})
    if answer.status_code == 200:
        return answer
    elif answer.status_code == 400:
        raise RuntimeError('Invalid ID supplied')
    elif answer.status_code == 404:
        raise RuntimeError('Pet not found')


def post_add_pet(dataxml):
    answer = requests.post('http://petstore.swagger.io/v2/pet', data=dataxml, headers={'accept': 'application/xml',
                                                                                      'Content-Type': 'application/xml'})
    if answer.status_code == 200:
        return answer
    elif answer.status_code == 405:
        raise RuntimeError('Invalid input')


def delete_pet(petID):
    answer = requests.delete('http://petstore.swagger.io/v2/pet/'+str(petID), headers={'accept': 'application/xml'})
    if answer.status_code == 200:
        return answer
    elif answer.status_code == 400:
        raise RuntimeError('Invalid ID supplied')
    elif answer.status_code == 404:
        raise RuntimeError('Pet not found')


