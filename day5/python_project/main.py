import requests
import json
import dicttoxml2

contact_service_url = 'https://vin-contact-service.herokuapp.com/api/contacts'


def f1():
    """
    Make a request to contact-service on heroku and get some response
    """
    resp = requests.get(contact_service_url)
    print(resp)


def f2():
    contact_id = '8ddb7fcf-0a7a-4eeb-a78f-13238ed85a77'
    url = f'{contact_service_url}/{contact_id}'
    r = requests.get(url)
    print(f'status code is {r.status_code}')
    print(r.text)


def f3():
    contact_id = '8ddb7fcf-0a7a-4eeb-a78f-13238ed85a77'
    url = f'{contact_service_url}/{contact_id}'
    headers = {'Accept': 'application/json'}
    # headers = {'Accept': 'text/plain'}
    # headers = {'Accept': 'application/xml'}

    r = requests.get(url, headers=headers)
    print(f'status code is {r.status_code}')
    print(r.text)


def f4():
    # params = {'city': 'Atlanta'}
    params = [('city', 'Atlanta')]
    headers = {'Accept': 'application/json'}
    r = requests.get(contact_service_url, params=params, headers=headers)
    print(f'status code is {r.status_code}')
    resp = r.json()
    for c in resp['contacts']:
        print(f'{"Mr." if c["gender"]=="Male" else "Ms."}{c["firstname"]} {c["lastname"]}')

    print(f'r.url is {r.url}')
    print(f'r.encoding is {r.encoding}')
    # r.encoding = 'ISO-8859-1'  # before accessing r.text, change the encoding to the required one


def f5():
    url = 'https://vinbasket.herokuapp.com/product-images/20001477_15-fresho-apple-shimla.jpg'
    r = requests.get(url)
    with open('apple.jpeg', 'wb') as f:
        f.write(r.content)  # binary content; do not use r.text
    print(f'status code is {r.status_code}')
    print('File saved to apple.jpeg')


def f6():
    new_contact = dict(firstname="Vinod", lastname="Kumar", email="vinod@vinod.co",
                       phone="9731424784", gender="Male", city="Bangalore")
    # (in the absence of Content-Type header, it will be assumed as form-data)
    r = requests.post(contact_service_url, data=new_contact)
    print(f'status code is {r.status_code}')
    print(r.text)


def f7():
    new_contact = dict(firstname="Vinod", lastname="Kumar", email="vinod1@vinod.co",
                       phone="9844083934", gender="Male", city="Bangalore")
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    r = requests.post(contact_service_url, data=json.dumps(new_contact), headers=headers)
    print(f'status code is {r.status_code}')
    print(r.text)


def f8():
    new_contact = dict(firstname="Vinod", lastname="Kumar", email="vinod2@vinod.co",
                       phone="8026661911", gender="Male", city="Bangalore")
    headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}

    xml = dicttoxml2.dicttoxml(new_contact, custom_root='contact', attr_type=False)
    r = requests.post(contact_service_url, data=xml, headers=headers)
    print(f'status code is {r.status_code}')
    print(r.text)

    print('Response headers are: ')
    for header in r.headers:
        print(f'{header} --> {r.headers[header]}')


def f9():
    params = {'email': 'vinod@vinod.co'}
    headers = {'Accept': 'application/json'}
    r = requests.get(contact_service_url, params=params, headers=headers)
    resp = r.json()
    print('Response from server: ')
    for k in resp:
        print(f'{k} --> {resp[k]}')

    resp['state'] = 'Karnataka'
    resp['address'] = '1st cross, 1st main, ISRO lyt'
    resp['country'] = 'India'
    resp['pincode'] = '560078'
    headers['Content-Type'] = 'application/json'
    r = requests.put(f'{contact_service_url}/{resp["id"]}', data=json.dumps(resp), headers=headers)
    print(f'status code for PUT request is {r.status_code}')
    print(f'PUT request url is {r.url}')
    print(json.dumps(r.json(), indent=3))


if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
    # f7()
    # f8()
    f9()
