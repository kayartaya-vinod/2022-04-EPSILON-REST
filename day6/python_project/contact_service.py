from flask import Flask, Response, request
import uuid
import json
import dicttoxml2

# create an object of class 'Flask'
app = Flask(__name__)
contacts = [
    dict(name='Vinod', email='vinod@vinod.co', phone='9731424784', city='Bangalore', id='341dabf3-7732-4f88-8853-8c795008e411'),
    dict(name='Shyam', email='shyam@xmpl.com', phone='9731498765', city='Shivamogga', id='4352e5cb-435c-4990-82bf-16f199f53052'),
    dict(name='Naveen', email='naveen@xmpl.com', phone='8761424784', city='Bangalore', id='f67da9d3-8a63-4734-badd-31a8f2daa2dc'),
    dict(name='John', email='john@xmpl.com', phone='9731412345', city='Dallas', id='c07d17e2-dea3-4cfb-a83a-9791d03736c2')
]


# simple custom method to produce json output
def create_json_response(data, status=200):
    return Response(json.dumps(data), status=status, mimetype='application/json')


# simple custom method to produce xml output
def create_xml_response(data, root='data', status=200):
    xml = dicttoxml2.dicttoxml(data, custom_root=root, attr_type=False)
    return Response(xml, status=status, mimetype='application/xml')


def create_response(data, status=200, root='data'):
    if request.headers['Accept'] == 'application/xml':
        return create_xml_response(data, root, status)
    return create_json_response(data, status)


@app.route('/api/contacts', methods=['GET'])
def get_all():
    # request.args --> query string parameters for the current request made by a client
    if 'city' in request.args:
        city = request.args['city']
        data = [c for c in contacts if c['city'] == city]
        return create_response(data, root='contacts')

    if 'email' in request.args:
        email = request.args['email']
        data = [c for c in contacts if c['email'] == email]
        data = None if len(data) == 0 else data[0]
        return create_response(data, root='contact')

    if 'phone' in request.args:
        phone = request.args['phone']
        data = [c for c in contacts if c['phone'] == phone]
        data = None if len(data) == 0 else data[0]
        return create_response(data, root='contact')

    return create_response(contacts, root='contacts')


@app.route('/api/contacts/<contact_id>')
def get_by_id(contact_id):
    data = [c for c in contacts if c['id'] == contact_id]
    if len(data) == 0:
        return create_response({'message': 'No data found!'}, status=404, root='error')
    return create_response(data[0], root='contact')


@app.route('/api/contacts', methods=['POST'])
def add_new_contact():
    payload = request.get_json()
    missing_fields = []
    if 'name' not in payload: missing_fields.append('name')
    if 'email' not in payload: missing_fields.append('email')
    if 'phone' not in payload: missing_fields.append('phone')

    if len(missing_fields) > 0:
        return create_json_response(f'These fields are missing in the payload - {missing_fields}', 400)

    if payload['name'].strip() == '':
        return create_json_response('"name" field cannot be blank', 400)
    if payload['email'].strip() == '':
        return create_json_response('"email" field cannot be blank', 400)
    if payload['phone'].strip() == '':
        return create_json_response('"phone" field cannot be blank', 400)

    data = [c for c in contacts if c['email'] == payload['email']]
    if len(data) > 0:
        return create_json_response('Contact with this email already exists!', 400)

    data = [c for c in contacts if c['phone'] == payload['phone']]
    if len(data) > 0:
        return create_json_response('Contact with this phone already exists!', 400)

    payload['id'] = str(uuid.uuid4())
    contacts.append(payload)

    return create_json_response(payload, 201)


@app.route('/api/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    for index, item in enumerate(contacts):
        if item['id'] == contact_id:
            break
    else:
        return create_json_response(f'No data found with id {contact_id}', 404)
    payload = request.get_json()
    payload['id'] = contact_id
    contacts[index] = payload  # replace the element at the found index with the payload
    return create_json_response(payload)


@app.route('/api/contacts/<contact_id>', methods=['PATCH'])
def patch_contact(contact_id):
    for index, item in enumerate(contacts):
        if item['id'] == contact_id:
            break
    else:
        return create_json_response(f'No data found with id {contact_id}', 404)
    payload = request.get_json()
    payload['id'] = contact_id
    contacts[index].update(payload)  # MERGE the payload with the element at the found index
    return create_json_response(contacts[index])


@app.route('/api/contacts/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    for index, item in enumerate(contacts):
        if item['id'] == contact_id:
            break
    else:
        return create_json_response(f'No data found with id {contact_id}', 404)
    deleted_contact = contacts.pop(index)
    return create_json_response(deleted_contact)


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # starts HTTP web server
