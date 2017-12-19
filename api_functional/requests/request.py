import requests


# def getapi(url):
#     answer = requests.get(url, headers={'accept': 'application/xml'})
#     if answer.status_code == 200:
#         return answer
#     elif answer.status_code == 400:
#         raise RuntimeError('Invalid ID supplied')
#     elif answer.status_code == 404:
#         raise RuntimeError('Pet not found')
def get(url, headers):
    return requests.get(url=url, headers=headers)


# def post_add_pet(dataxml):
#     answer = requests.post('http://petstore.swagger.io/v2/pet', data=dataxml, headers={'accept': 'application/xml',
#                                                                                       'Content-Type': 'application/xml'})
#     if answer.status_code == 200:
#         return answer
#     elif answer.status_code == 405:
#         raise RuntimeError('Invalid input')
def post(url, data_xml, headers):
    return requests.post(url=url, data=data_xml, headers=headers)


# def delete_pet(petID):
#     answer = requests.delete('http://petstore.swagger.io/v2/pet/'+str(petID), headers={'accept': 'application/xml'})
#     if answer.status_code == 200:
#         return answer
#     elif answer.status_code == 400:
#         raise RuntimeError('Invalid ID supplied')
#     elif answer.status_code == 404:
#         raise RuntimeError('Pet not found')
def delete(url, headers):
    return requests.delete(url=url, headers=headers)
    # if answer.status_code == 200:
    #     return answer
    # elif answer.status_code == 400:
    #     raise RuntimeError('Invalid ID supplied')
    # elif answer.status_code == 404:
    #     raise RuntimeError('Pet not found')


# TODO implement put request
def put(url, headers):
    pass
