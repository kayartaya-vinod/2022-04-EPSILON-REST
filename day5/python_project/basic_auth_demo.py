import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/vinod/topsecret'


def f1():
    r = requests.get(url)
    print(f'status code is {r.status_code}')
    print(r.text)

    r = requests.get(url, auth=HTTPBasicAuth('vinod', 'topsecret'))
    print(f'status code is {r.status_code}')
    print(r.text)

    # considered as a new client; and hence need to send basic auth information again
    r = requests.get(url)
    print(f'status code is {r.status_code}')
    print(r.text)


def f2():
    session = requests.Session()
    # using this session, we may make multiple requests
    # all of them are considered as part of a single user session
    session.auth = ('vinod', 'topsecret')
    r = session.get(url)
    print(f'status code is {r.status_code}')
    print(r.text)

    r = session.get(url)
    print(f'status code is {r.status_code}')
    print(r.text)

    session.close()


if __name__ == '__main__':
    f2()
