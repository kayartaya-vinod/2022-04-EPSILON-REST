import unittest
import requests
import json

base_url = 'https://vinbasket.herokuapp.com'
orders_url = f'{base_url}/orders'
login_url = f'{base_url}/login'


class TestOrderService(unittest.TestCase):

    def setUp(self) -> None:
        user = json.dumps({'email': 'vinod@vinod.co', 'password': 'topsecret'})
        headers = {'Content-Type': 'application/json'}
        r = requests.post(login_url, data=user, headers=headers)
        resp = r.json()
        self.token = resp['token']

    def xtest_should_get_unauthorized_error(self):
        r = requests.get(orders_url)
        self.assertEqual(r.status_code, requests.codes.unauthorized)

    def xtest_should_get_orders(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        r = requests.get(orders_url, headers=headers)
        self.assertEqual(r.status_code, requests.codes.ok)
        resp = r.json()
        # self.assertEqual(len(resp), 6)

    def test_should_get_order_by_id(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        r = requests.get(orders_url+'/1', headers=headers)
        order = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(len(order['lineItems']), 3)
        product1 = order['lineItems'][0]['product']
        self.assertEqual(product1['unit_price'], 110)


if __name__ == '__main__':
    unittest.main()
