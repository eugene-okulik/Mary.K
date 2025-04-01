import requests


url = 'http://167.172.172.115:52353/object'


def create_obj():
    payload = {
        'data': {'color': 'yellow', 'size': 'medium'},
        'name': 'object 1'
    }
    headers = {'Content-Type': 'application/json'}
    return str(requests.post(url, json=payload, headers=headers).json()['id'])


def clear(obj_id):
    return requests.delete(url + '/' + obj_id)


def post_object():
    payload = {
        'data': {'color': 'yellow', 'size': 'medium'},
        'name': 'object 1'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, f'Status code {response.status_code} is not equal to 200'
    assert response.json()['name'] == 'object 1', 'The object name is incorrect'

    clear(str(response.json()['id']))


def put_object():
    obj_id = create_obj()
    payload = {
        'data': {'color': 'daffodil yellow', 'size': 'XL'},
        'name': 'object 1.1'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url + '/' + obj_id, json=payload, headers=headers)

    assert response.status_code == 200, f'Status code {response.status_code} is not equal to 200'
    assert response.json()['data']['color'] == 'daffodil yellow', 'The color is incorrect'
    assert response.json()['data']['size'] == 'XL', 'The size is incorrect'
    assert response.json()['name'] == 'object 1.1', 'The object name is incorrect'

    clear(obj_id)


def patch_object():
    obj_id = create_obj()
    payload = {
        'data': {'color': 'canary yellow', 'size': 'XL', 'shape': 'round'},
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(url + '/' + obj_id, json=payload, headers=headers)

    assert response.status_code == 200, f'Status code {response.status_code} is not equal to 200'
    assert response.json()['data']['color'] == 'canary yellow', 'The color is incorrect'
    assert response.json()['data']['size'] == 'XL', 'The size is incorrect'
    assert response.json()['data']['shape'] == 'round', 'The shape is incorrect'
    assert response.json()['name'] == 'object 1', 'The object name is incorrect'

    clear(obj_id)


def delete_object():
    obj_id = create_obj()
    response = requests.delete(url + '/' + obj_id)

    assert response.status_code == 200, f'Status code {response.status_code} is not equal to 200'


post_object()
put_object()
patch_object()
delete_object()
