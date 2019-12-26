from aiohttp import web
import pytest, json
from app.__main__ import routes


@pytest.fixture
def cli(aiohttp_client, loop):
    app = web.Application()
    app.add_routes(routes)
    return loop.run_until_complete(aiohttp_client(app))


# PETS ENDPOINTS TESTS

async def test_get_pets_handler_success(cli):
    # Act
    resp = await cli.get('/pets?type=cat')
    json_response = json.loads(await resp.text())
    # Assert
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    assert all(jresp['type'] == 'cat' for jresp in json_response)


async def test_get_pets_handler_wrong_endpoint(cli):
    # Act
    resp = await cli.get('/pet?type=cat')
    # Assert
    assert resp.status == 404


async def test_get_pets_handler_wrong_type(cli):
    # Act
    resp = await cli.get('/pets?type=qweqweqwe')
    # Assert
    assert resp.status == 204


async def test_get_pet_handler_success(cli):
    # Act
    resp = await cli.get('/pets/b7b650c4-c274-11e9-89fa-634d818dbd9d')
    json_response = json.loads(await resp.text())
    # Assert
    print(resp.content_type)
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    assert json_response['name'] == 'Bürek'


async def test_get_pet_handler_wrong_endpoint(cli):
    # Act
    resp = await cli.get('/pet/b7b650c4-c274-11e9-89fa-634d818dbd9d')
    # Assert
    assert resp.status == 404


async def test_get_pet_handler_wrong_id(cli):
    # Act
    resp = await cli.get('/pets/09090909090909bledneId')
    # Assert
    assert resp.status == 204


async def test_add_pet_handler_success(cli):
    # Act
    resp = await cli.post('/pets', data='''
    {
        "id": "998",
        "name": "yaro",
        "type": "dog",
        "available": true,
        "addedAt": "2019-08-19 12:31:12",
        "adoptedAt": null,
        "description": "owczarek polski, ładny piesek, nie ma pcheł",
        "shelterId": "bd09b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')
    # Assert
    assert resp.status == 201


async def test_add_pet_handler_already_exists_error(cli):
    # Act
    resp = await cli.post('/pets', data='''
    {
        "id": "998",
        "name": "yaro",
        "type": "dog",
        "available": true,
        "addedAt": "2019-08-19 12:31:12",
        "adoptedAt": null,
        "description": "owczarek polski, ładny piesek, nie ma pcheł",
        "shelterId": "bd09b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')
    # Assert
    assert resp.status == 409


async def test_update_pet_handler_success(cli):
    # Act
    resp = await cli.patch('/pets', data='''
    {
        "id": "999",
        "name": "maro",
        "type": "dog",
        "available": true,
        "addedAt": "2019-09-19 12:31:12",
        "adoptedAt": null,
        "description": "owczarek polski, ładny piesek, nie ma pcheł",
        "shelterId": "b999b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')

    # Assert
    assert resp.status == 204

async def test_update_partly_pet_handler_success(cli):
    # Act
    resp = await cli.patch('/pets', data='''
    {
        "id": "999",
        "name": "maro",
        "shelterId": "b999b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')

    # Assert
    assert resp.status == 204


async def test_update_pet_handler_wrong_request_body(cli):
    # Act
    resp = await cli.patch('/pets', data='''
    {
        "id": "999",
        "name": "maro",
        "tpe": "dog",
        "available": true,
        "addedAt": "2019-08-19 12:31:12",
        "adoptedAt": null,
        "descrption": "owczarek polski, ładny piesek, nie ma pcheł",
        "shelterId": "bd09b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')

    # Assert
    assert resp.status == 400

async def test_update_pet_handler_no_id(cli):
    # Act
    resp = await cli.patch('/pets', data='''
    {
        "addedAt": "2019-08-19 12:31:12",
        "adoptedAt": null,
        "descrption": "owczarek polski, ładny piesek, nie ma pcheł",
        "shelterId": "bd09b2f0-c274-11e9-963b-6b7b4dc28ba0"
    }''')

    # Assert
    assert resp.status == 400


async def test_delete_pet_handler_success(cli):
    # Act
    resp = await cli.delete('/pets/998')

    # Assert
    assert resp.status == 204


async def test_delete_pet_handler_error(cli):
    # Act
    resp = await cli.delete('/pets/09090909090909bledneId')

    # Assert
    assert resp.status == 404


# SHELTERS ENDPOINTS TESTS

async def test_get_shelters_handler_success(cli):
    # Act
    resp = await cli.get('/shelters?city=Warszawa')
    json_response = json.loads(await resp.text())
    # Assert
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    assert all(jresp['city'] == 'Warszawa' for jresp in json_response)


async def test_get_shelters_handler_wrong_endpoint_error(cli):
    # Act
    resp = await cli.get('/shelter?city=Warszawa')
    # Assert
    assert resp.status == 404


async def test_get_shelters_handler_wrong_city_error(cli):
    # Act
    resp = await cli.get('/shelters?city=poaspdoapsdoapsd')
    # Assert
    assert resp.status == 204


async def test_get_shelter_handler_success(cli):
    # Act
    resp = await cli.get('/shelters/bd09b2f0-c274-11e9-963b-6b7b4dc28ba0')
    json_response = json.loads(await resp.text())
    # Assert
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    assert json_response['name'] == 'Schronisko Pod Lipą'


async def test_get_shelter_handler_wrong_endpoint(cli):
    # Act
    resp = await cli.get('/shelter/b7b650c4-c274-11e9-89fa-634d818dbd9d')
    # Assert
    assert resp.status == 404


async def test_get_shelter_handler_wrong_id(cli):
    # Act
    resp = await cli.get('/shelters/09blablabbledneId')
    # Assert
    assert resp.status == 204


async def test_get_pets_by_shelter_handler_success(cli):
    # Act
    resp = await cli.get('/shelters/bd09b2f0-c274-11e9-963b-6b7b4dc28ba0/pets')
    json_response = json.loads(await resp.text())
    # Assert
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    assert all(jresp['shelterId'] ==
               'bd09b2f0-c274-11e9-963b-6b7b4dc28ba0' for jresp in json_response)


async def test_get_pets_by_shelter_handler_wrong_id(cli):
    # Act
    resp = await cli.get('/shelters/bd09b2bledneidb7b4dc28ba0/pets')
    # Assert
    assert resp.status == 204


async def test_add_shelter_handler_success(cli):
    # Act
    resp = await cli.post('/shelters', data='''
    {
        "id": "nowenowenoweid",
        "name": "Schroniskasdaso Pod Lipą",
        "fullAddress": "uldasdasd. Lipowa 18, 00-123 Będzin",
        "city": "Będzasdasdin",
        "petsAvailable": 123
    }''')
    # Assert
    assert resp.status == 201


async def test_add_shelter_handler_already_exists_error(cli):
    # Act
    resp = await cli.post('/shelters', data='''
    {
        "id": "bd09b2f0-c274-11e9-963b-6b7b4dc28ba0",
        "name": "Schronisko Pod Lipą",
        "fullAddress": "ul. Lipowa 18, 00-123 Będzin",
        "city": "Będzin",
        "petsAvailable": 13
    }''')
    # Assert
    assert resp.status == 409
