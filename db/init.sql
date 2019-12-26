CREATE TABLE pets("id" text NOT NULL, "name" text, "type" text NOT NULL, "available" boolean NOT NULL, "addedAt" text, "adoptedAt" text, "description" text, "shelterId" text NOT NULL, PRIMARY KEY (id)) WITH (OIDS = FALSE);
ALTER TABLE  pets OWNER to postgres;
CREATE TABLE shelters("id" text NOT NULL, "name" text NOT NULL, "fullAddress" text NOT NULL, "city" text NOT NULL, "petsAvailable" int NOT NULL, PRIMARY KEY (id)) WITH (OIDS = FALSE);
ALTER TABLE pets OWNER to postgres;
INSERT INTO pets VALUES('b7b650c4-c274-11e9-89fa-634d818dbd9d', 'Bürek', 'dog', true, '2017-08-19 12:31:12', null, 'owczarek niemiecki, ładny piesek, nie ma pcheł', 'bd09b2f0-c274-11e9-963b-6b7b4dc28ba0');
INSERT INTO pets VALUES('b192136f-fd5b-9bba-c7e3-d552cef15f42', 'Sznurek', 'cat', true, '2019-08-20 12:31:12', null, 'ragdoll, milusi, skoczny', 'bd09b2f0-c274-11e9-963b-6b7b4dc28ba0');
INSERT INTO pets VALUES('e833d34c-d384-3a75-9f51-4a88bfae8d85', 'Pazurek', 'dog', true, '2018-08-21 12:31:12', null, 'owczarek polski, ładny piesek, nie ma pcheł', 'bd09b2f0-c274-11e9-963b-6b7b4dc28ba0');
INSERT INTO pets VALUES('ef1df1b2-3840-e713-1756-041839fb9a14', 'Benjamin', 'cat', true, '2009-08-22 12:31:12', null, 'dachowiec, ładny, nie ma pcheł', '8070c1fd-d945-e2cd-1c84-98958f6673a1');
INSERT INTO pets VALUES('4710717a-4bc7-5eed-181a-308122b210ee', 'Pablo', 'cat', true, '2014-08-23 12:31:12', null, 'dachowiec, ładny, nie ma pcheł', '8070c1fd-d945-e2cd-1c84-98958f6673a1');
INSERT INTO pets VALUES('e651d810-2fbb-e85a-771e-bc8e7465d139', 'Szarik', 'dog', true, '2015-08-24 12:31:12', null, 'owczarek hiszpański, ładny piesek, nie ma pcheł', '2cf8e8fd-6ed8-66f2-7d70-eb93a2ff92a9');
INSERT INTO pets VALUES('111a29d6-2414-635f-ed11-0a3f8a3a622e', 'Wezuwiusz', 'dog', true, '2017-08-25 12:31:12', null, 'owczarek angielski, ładny piesek, nie ma pcheł', '2cf8e8fd-6ed8-66f2-7d70-eb93a2ff92a9');
INSERT INTO pets VALUES('a37bc497-c347-a6b4-4d19-cbe2a2251f80', 'Jeremi', 'cat', true, '2019-08-26 12:31:12', null, 'dachowiec, nie ma pcheł', '2cf8e8fd-6ed8-66f2-7d70-eb93a2ff92a9');
INSERT INTO pets VALUES('a27367dc-868b-0b22-4399-2ed9e2dbc505', 'Stefan', 'dog', true, '2019-08-27 12:31:12', null, 'owczarek irlandzki, ładny piesek, nie ma pcheł', '2cf8e8fd-6ed8-66f2-7d70-eb93a2ff92a9');
INSERT INTO shelters VALUES('bd09b2f0-c274-11e9-963b-6b7b4dc28ba0', 'Schronisko Pod Lipą', 'ul. Lipowa 18, 00-123 Będzin', 'Będzin', 3);
INSERT INTO shelters VALUES('8070c1fd-d945-e2cd-1c84-98958f6673a1', 'Koci Raj', 'ul. Zakryta 11, 01-123 Warszawa', 'Warszawa', 2);
INSERT INTO shelters VALUES('2cf8e8fd-6ed8-66f2-7d70-eb93a2ff92a9', 'Psie Marzenie', 'ul. Odkryta 23, 02-123 Wrocław', 'Wrocław', 4);