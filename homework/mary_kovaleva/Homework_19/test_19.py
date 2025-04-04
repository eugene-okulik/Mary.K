import requests
import pytest

url = 'http://167.172.172.115:52353/object'


@pytest.fixture()
def obj_id():
    payload = {
        'data': {'color': 'yellow', 'size': 'medium'},
        'name': 'object 1'
    }
    headers = {'Content-Type': 'application/json'}
    obj_id = str(requests.post(url, json=payload, headers=headers).json()['id'])
    print('The object is created')
    yield obj_id
    requests.delete(url + '/' + obj_id)
    print('The object is deleted')


@pytest.fixture(scope='session')
def print_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def print_function():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
@pytest.mark.parametrize('objects', [
    {'data': {'color': 'yellow', 'size': 'medium'}, 'name': 'object 1'},
    {'data': {'color': 'black', 'size': 'XS'}, 'name': 'object 2'},
    {'data': {'color': 'purple', 'size': 'gigantic'}, 'name': 'object 3'}
])
def test_post_object(print_session, print_function, objects):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=objects, headers=headers)

    assert response.status_code == 200, f'Status code {response.status_code} is not equal to 200'
    assert response.json()['name'] == objects['name'], 'The object name is incorrect'


def test_put_object(print_function, obj_id):
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


@pytest.mark.medium
def test_patch_object(print_function, obj_id):
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


def test_delete_object(print_function, obj_id):
    response = requests.delete(url + '/' + obj_id)

    assert response.status_code == 200, f'Status code {response.status_code} != 200'
