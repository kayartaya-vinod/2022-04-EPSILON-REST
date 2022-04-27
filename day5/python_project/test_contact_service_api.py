import json

import dicttoxml2
import requests
import unittest

contact_service_url = 'https://vin-contact-service.herokuapp.com/api/contacts'


class TestContactServiceForGetRequests(unittest.TestCase):

    def setUp(self) -> None:
        self.r = requests.get(contact_service_url)

    def test_should_get_ok_response(self):
        self.assertEqual(self.r.status_code, requests.codes.ok)

    def test_should_get_json_response_header(self):
        actual = self.r.headers['Content-Type']
        expected = 'application/json'
        self.assertEqual(self.r.status_code, requests.codes.ok)
        self.assertEqual(actual, expected)

    def test_should_get_xml_response_header(self):
        r = requests.get(contact_service_url, headers={'Accept': 'application/xml'})
        actual = r.headers['Content-Type']
        expected = 'application/xml'
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(actual, expected)


class TestContactServiceForPostRequests(unittest.TestCase):

    def tearDown(self) -> None:
        params = {'email': 'vinod@vinod.co'}
        headers = {'Accept': 'application/json'}
        r = requests.get(contact_service_url, params=params, headers=headers)
        c = r.json()
        requests.delete(contact_service_url+'/' + c['id'])

    def test_should_add_new_contact_as_json(self):
        new_contact = {'firstname': 'Vinod', 'lastname': 'Kumar', 'email': 'vinod@vinod.co', 'phone': '9731424784'}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(contact_service_url, data=json.dumps(new_contact), headers=headers)
        nc = r.json()
        self.assertEqual(r.status_code, 201)
        self.assertIsNotNone(nc['id'])
        self.assertEqual(nc['email'], 'vinod@vinod.co')

    def test_should_add_new_contact_as_form_data(self):
        new_contact = {'firstname': 'Vinod', 'lastname': 'Kumar', 'email': 'vinod@vinod.co', 'phone': '9731424784'}
        r = requests.post(contact_service_url, data=new_contact)
        nc = r.json()
        self.assertEqual(r.status_code, 201)
        self.assertIsNotNone(nc['id'])
        self.assertEqual(nc['email'], 'vinod@vinod.co')

    def test_should_add_new_contact_as_xml(self):
        new_contact = {'firstname': 'Vinod', 'lastname': 'Kumar', 'email': 'vinod@vinod.co', 'phone': '9731424784'}
        headers = {'Content-Type': 'application/xml', 'Accept': 'application/json'}
        xml = dicttoxml2.dicttoxml(new_contact, custom_root='contact', attr_type=False)
        r = requests.post(contact_service_url, data=xml.decode('utf-8'), headers=headers)
        nc = r.json()
        self.assertEqual(r.status_code, 201)
        self.assertIsNotNone(nc['id'])
        self.assertEqual(nc['email'], 'vinod@vinod.co')


if __name__ == '__main__':
    unittest.main()
