# **Indoorway rekrutacja**

## run `docker-compose up` to start the api & db

### to run tests

1. run `pip install aiohttp pytest pytest-aiohttp`
2. ensure that the api & db are running
3. run `pytest`

***

#### API is not prone to SQL injection attacks due to use of parameterized queries

#### You might want to add the following directive to the docker-compose.yaml for development

```docker
volumes:
    - ./app:/usr/src/app
```

***

## API docs

GET /pets (?type=dog, ?shelterId=bd09b2f0-c274-11e9-963b-6b7b4dc28ba0)
pobranie listy zwierząt z opcją filtrowania po polach “type” oraz “shelterId”

GET /pets/&lt;id&gt;
pobranie informacji o zwierzęciu

POST /pets
dodanie nowego zwierzęcia
request body: obiekt zgodny ze "strukturą obiektu pet" podanego poniżej, np.
`{
    “id”: hex123hex-c274-11e9-89fa-634d818dbd9d”,
    “name”: “Nowy”,
    “type”: cat,
    “available”: true,
    “addedAt”: “2019-08-19 12:31:12”,
    “adoptedAt”: null,
    “description”: “owczarek niemiecki, ładny piesek, nie ma pcheł”,
    “shelterId”: “bd09b2f0-c274-11e9-963b-6b7b4dc28ba0”
}`

PATCH /pets
aktualizacja danych o zwierzęciu
request body: json z id i danymi, które chcemy zmienić, np.
`{"id": "b7b650c4-c274-11e9-89fa-634d818dbd9d", "name": "Marian"}`

DELETE /pets/&lt;id&gt;
usunięcie zwierzęcia

GET /shelters (?city=warszawa)
pobranie listy schronisk z opcją filtrowania po polu “city”

GET /shelters/&lt;id&gt;
pobranie informacji o schronisku

GET /shelters/&lt;id&gt;/pets (?type=dog)
pobranie listy zwierząt z danego schroniska z opcją filtrowania po polu “type”

POST /shelters
dodanie nowego schroniska
request body: obiekt zgodny ze "strukturą obiektu shelter" podanego poniżej, np.
`{
    “id”: hexhexhe-c274-11e9-963b-6b7b4dc28ba0”,
    “name”: “Nowe Schronisko”,
    “fullAddress”: “ul. Lipowa 18, 00-123 Katowice”,
    “city”: “Katowice”,
    “petsAvailable”: 13
}`

Struktura obiektu “pet”:
`{
    “id”: “b7b650c4-c274-11e9-89fa-634d818dbd9d”,
    “name”: “Bürek”,
    “type”: “dog”,
    “available”: true,
    “addedAt”: “2019-08-19 12:31:12”,
    “adoptedAt”: null,
    “description”: “owczarek niemiecki, ładny piesek, nie ma pcheł”,
    “shelterId”: “bd09b2f0-c274-11e9-963b-6b7b4dc28ba0”
}`

Struktura obiektu “shelter”:
`{
    “id”: “bd09b2f0-c274-11e9-963b-6b7b4dc28ba0”,
    “name”: “Schronisko Pod Lipą”,
    “fullAddress”: “ul. Lipowa 18, 00-123 Będzin”,
    “city”: “Będzin”,
    “petsAvailable”: 13
}`
