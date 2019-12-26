import psycopg2, os

test = "test_app.py" in os.listdir(os.path.abspath('.'))

async def get_connection():

    if test:
        connection = psycopg2.connect(user="postgres",
                                  password="mysecretpassword",
                                      host="localhost",
                                      port="5432",
                                  database="postgres")

    else:
        connection = psycopg2.connect(user="postgres",
                                  password="mysecretpassword",
                                      host="db-service",
                                      port="5432",
                                  database="postgres")

    return connection


# PETS CRUD

async def get_pets(query):
    connection = await get_connection()
    cursor = connection.cursor()

    if 'type' in query.keys() and 'shelterId' in query.keys():
        cursor.execute(
            '''
            SELECT * FROM pets
            WHERE type = %s
            AND "shelterId" = %s;
            ''', (query['type'], query['shelterId']))

    elif 'type' in query.keys() and 'shelterId' not in query.keys():
        cursor.execute(
            '''
            SELECT * FROM pets
            WHERE type = %s;
            ''', (query['type'],))

    elif 'shelterId' in query.keys() and 'type' not in query.keys():
        cursor.execute(
            '''
            SELECT * FROM pets
            WHERE "shelterId" = %s;
            ''', (query['shelterId'],))

    else:
        cursor.execute("SELECT * FROM pets;")

    pets = cursor.fetchall()
    pets_list = [{
        "id": pet[0],
        "name": pet[1],
        "type": pet[2],
        "available": pet[3],
        "addedAt": pet[4],
        "adoptedAt": pet[5],
        "description": pet[6],
        "shelterId": pet[7]
    } for pet in pets]

    cursor.close()
    connection.close()

    return pets_list


async def get_pet(id: str):
    connection = await get_connection()
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM pets
        WHERE id = %s;
        ''', (id,))

    try:
        pet = cursor.fetchall()[0]
    except:
        return False

    pet_dict = {
        "id": pet[0],
        "name": pet[1],
        "type": pet[2],
        "available": pet[3],
        "addedAt": pet[4],
        "adoptedAt": pet[5],
        "description": pet[6],
        "shelterId": pet[7]
    }
    cursor.close()
    connection.close()

    return pet_dict


async def add_pet(id, name, type, available, addedAt,
                  adoptedAt, description, shelterId):

    connection = await get_connection()
    cursor = connection.cursor()

    if adoptedAt == None:
        adopted_at = 'null'
    else:
        adopted_at = adoptedAt
    try:
        cursor.execute(
            '''
            INSERT INTO pets VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
            ''', (id, name, type, available, addedAt, adopted_at.strip(''),
                  description, shelterId))

    except: return False
    connection.commit()

    cursor.close()
    connection.close()

    return True


async def update_pet(id, name = False, type = False, available = False, addedAt = False,
                     adoptedAt = False, description = False, shelterId = False):

    connection = await get_connection()
    cursor = connection.cursor()

    try:
        if name: cursor.execute('''UPDATE pets SET "name" = %s WHERE id = %s;''', (name, id,))
        if type: cursor.execute('''UPDATE pets SET "type" = %s WHERE id = %s;''', (type, id,))
        if available: cursor.execute('''UPDATE pets SET "available" = %s WHERE id = %s;''', (available, id,))
        if addedAt: cursor.execute('''UPDATE pets SET "addedAt" = %s WHERE id = %s;''', (addedAt, id,))
        if adoptedAt: cursor.execute('''UPDATE pets SET "adoptedAt" = %s WHERE id = %s;''', (adoptedAt, id,))
        if description: cursor.execute('''UPDATE pets SET "description" = %s WHERE id = %s;''', (description, id,))
        if shelterId: cursor.execute('''UPDATE pets SET "shelterId" = %s WHERE id = %s;''', (shelterId, id,))

    except: return False

    connection.commit()

    cursor.close()
    connection.close()

    return True


async def delete_pet(id: str):

    connection = await get_connection()
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM pets
        WHERE id = %s;
        ''', (id,))

    try: pet = cursor.fetchall()[0]
    except: return False

    try:
        cursor.execute(
            '''
            DELETE FROM pets
            WHERE id = %s;
            ''', (id,))

    except: return False

    connection.commit()

    cursor.close()
    connection.close()

    return True


# SHELTERS CRUD

async def get_shelters(query):
    connection = await get_connection()
    cursor = connection.cursor()
    if 'city' in query.keys():
        cursor.execute(
            '''
            SELECT * FROM shelters
            WHERE "city" = %s;
            ''', (query['city'],))

    else: cursor.execute("SELECT * FROM shelters;")

    shelters = cursor.fetchall()
    shelters_list = [{
        "id": shelter[0],
        "name": shelter[1],
        "fullAddress": shelter[2],
        "city": shelter[3],
        "petsAvailable": shelter[4]

    } for shelter in shelters]

    cursor.close()
    connection.close()

    return shelters_list


async def get_shelter(id: str):

    connection = await get_connection()
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM shelters
        WHERE "id" = %s;
        ''', (id,))

    try: shelter = cursor.fetchall()[0]
    except: return False

    shelter_dict = {
        "id": shelter[0],
        "name": shelter[1],
        "fullAddress": shelter[2],
        "city": shelter[3],
        "petsAvailable": shelter[4]
    }

    cursor.close()
    connection.close()

    return shelter_dict


async def get_pets_by_shelter(id: str, query: dict):

    connection = await get_connection()
    cursor = connection.cursor()

    if 'type' in query.keys():
        cursor.execute(
            '''
            SELECT * FROM pets
            WHERE "shelterId" = %s
            AND "type" = %s;
             ''', (id, query['type']))

    else:
        cursor.execute(
            '''
            SELECT * FROM pets WHERE "shelterId" = %s;
             ''', (id,))

    pets = cursor.fetchall()
    pets_list = [{
        "id": pet[0],
        "name": pet[1],
        "type": pet[2],
        "available": pet[3],
        "addedAt": pet[4],
        "adoptedAt": pet[5],
        "description": pet[6],
        "shelterId": pet[7]
    } for pet in pets]

    cursor.close()
    connection.close()

    return pets_list


async def add_shelter(id, name, fullAddress, city, petsAvailable):

    connection = await get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO shelters VALUES(%s, %s, %s, %s, %s);
            ''', (id, name, fullAddress, city, petsAvailable))

    except: return False

    connection.commit()

    cursor.close()
    connection.close()

    return True
