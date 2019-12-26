import json
from aiohttp import web
from . import crud


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text='try requesting /pets '
                           + ' /shelters resources!')


# PETS ENDPOINTS

@routes.get('/pets')
async def get_pets_handler(request):
    query = dict(request.rel_url.query.copy())
    pets = await crud.get_pets(query)
    if pets == []: return web.Response(status=204)
    return web.json_response(pets)


@routes.get('/pets/{id}')
async def get_pet_handler(request):
    pet = await crud.get_pet(request.match_info['id'])
    if not pet: return web.Response(status=204)
    return web.json_response(pet)


@routes.post('/pets')
async def add_pet_handler(request):
    data = await request.read()
    data_dict = json.loads(data.decode('utf-8'))
    successful = await crud.add_pet(**data_dict)
    if not successful: return web.Response(status=409)
    return web.Response(status=201)


@routes.patch('/pets')
async def update_pet_handler(request):
    data = await request.read()
    data_dict = json.loads(data.decode('utf-8'))
    try: successful = await crud.update_pet(**data_dict)
    except: return web.Response(status=400)
    if not successful: return web.Response(status=400)
    return web.Response(status=204)


@routes.delete('/pets/{id}')
async def delete_pet_handler(request):
    successful = await crud.delete_pet(request.match_info['id'])
    if not successful: return web.Response(status=404)
    return web.Response(status=204)


# SHELTERS ENDPOINTS

@routes.get('/shelters')
async def get_shelters_handler(request):
    query = dict(request.rel_url.query.copy())
    shelters = await crud.get_shelters(query)
    if shelters == []: return web.Response(status=204)
    return web.json_response(shelters)


@routes.get('/shelters/{id}')
async def get_shelter_handler(request):
    shelter = await crud.get_shelter(request.match_info['id'])
    if not shelter: return web.Response(status=204)
    return web.json_response(shelter)


@routes.get('/shelters/{id}/pets')
async def get_pets_by_shelter_handler(request):
    pets = await crud.get_pets_by_shelter(request.match_info['id'], dict(request.rel_url.query.copy()))
    if pets == []: return web.Response(status=204)
    return web.json_response(pets)


@routes.post('/shelters')
async def add_shelter_handler(request):
    data = await request.read()
    data_dict = json.loads(data.decode('utf-8'))
    successful = await crud.add_shelter(**data_dict)
    if not successful: return web.Response(status=409)
    return web.Response(status=201)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='0.0.0.0', port='8000')