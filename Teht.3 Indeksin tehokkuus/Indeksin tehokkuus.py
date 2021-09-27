import sqlite3
import time
import datetime
import random
import string


db = sqlite3.connect("indeksi.db")
db.isolation_level = None



def random_elokuva():

    kirjaimet = string.ascii_letters.lower()

    elokuva_nimi = ""

    for i in range(0,8):
        elokuva_nimi += random.choice(kirjaimet)
    
    return elokuva_nimi

def random_vuosi():

    vuosi = random.randint(1900,2000)

    return vuosi



def ohjelma_ilman_indeksia():

    start_time = time.time()


    db.execute("BEGIN")

    db.execute(f"CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")

    rivien_lisays_start = time.time()

    for i in range(1,1000000+1):
        db.execute(f"INSERT INTO Elokuvat (nimi,vuosi) VALUES ('{random_elokuva()}', {random_vuosi()})")

    rivien_lisays_end = time.time() - rivien_lisays_start   
    kysely_start = time.time()

    for i in range(1,1000+1):
        db.execute(f"SELECT COUNT(nimi) FROM Elokuvat WHERE vuosi = {random_vuosi()}")

    kysely_end = time.time() - kysely_start   
    db.execute("COMMIT")


    print(f"Rivien lisäykseen kulunut aika: {rivien_lisays_end}")
    print(f"Kyselyn suoritukseen kulunut aika: {kysely_end}")
    print(f"Ohjelman suorittamiseen kulunut aika ilman kyselyitä tehostavaa indeksiä: {time.time()-start_time}")

# ohjelma_ilman_indeksia()

#   Ohjelman suorittamiseen ilman indeksiä meni 60.358635663986206 sekunttia
#   testi#2  58.89056062698364 sekunttia

def ohjelma_indeksilla_ennen_rivien_lisaamista():

    start_time = time.time()


    db.execute("BEGIN")

    db.execute(f"CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")
    # db.execute(f"CREATE INDEX idx_nimi ON Elokuvat (nimi)")
    # db.execute(f"CREATE INDEX idx_vuosi ON Elokuvat (vuosi)")
    db.execute(f"CREATE INDEX idx_vuosi ON Elokuvat (vuosi, nimi)")

    rivien_lisays_start = time.time()

    for i in range(1,1000000+1):
        db.execute(f"INSERT INTO Elokuvat (nimi,vuosi) VALUES ('{random_elokuva()}', {random_vuosi()})")
    
    rivien_lisays_end = time.time() - rivien_lisays_start
    
    kysely_start = time.time()

    for i in range(1,1000+1):
        db.execute(f"SELECT COUNT(nimi) FROM Elokuvat WHERE vuosi = {random_vuosi()}")
    
    kysely_end = time.time() - kysely_start
    
    db.execute("COMMIT")


    print(f"Rivien lisäykseen kulunut aika: {rivien_lisays_end}")
    print(f"Kyselyn suoritukseen kulunut aika: {kysely_end}")
    print(f"Ohjelman suorittamiseen kulunut aika kun kyselyitä tehostavat indeksit on lisätty ennen rivien lisäämistä: {time.time()-start_time}")

# ohjelma_indeksilla_ennen_rivien_lisaamista()
#   Kun indeksit lisättiin 
#   Rivien lisäykseen kulunut aika: 26.029778957366943
#   Kyselyn suoritukseen kulunut aika: 0.7335555553436279
#   Ohjelman suorittamiseen kulunut aika kun kyselyitä tehostavat indeksit on lisätty ennen rivien lisäämistä: 26.84013032913208


def ohjelma_indeksilla_ennen_kyselyita():

    start_time = time.time()


    db.execute("BEGIN")

    db.execute(f"CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")


    rivien_lisays_start = time.time()

    for i in range(1,1000000+1):
        db.execute(f"INSERT INTO Elokuvat (nimi,vuosi) VALUES ('{random_elokuva()}', {random_vuosi()})")
    
    rivien_lisays_end = time.time() - rivien_lisays_start
    
    kysely_start = time.time()

    db.execute(f"CREATE INDEX idx_vuosi ON Elokuvat (vuosi, nimi)")

    for i in range(1,1000+1):
        db.execute(f"SELECT COUNT(nimi) FROM Elokuvat WHERE vuosi = {random_vuosi()}")
    
    kysely_end = time.time() - kysely_start
    
    db.execute("COMMIT")


    print(f"Rivien lisäykseen kulunut aika: {rivien_lisays_end}")
    print(f"Kyselyn suoritukseen kulunut aika: {kysely_end}")
    print(f"Ohjelman suorittamiseen kulunut aika kun kyselyitä tehostavat indeksit on lisätty ennen kyselyitten suorittamista: {time.time()-start_time}")

ohjelma_indeksilla_ennen_kyselyita()

#   Rivien lisäykseen kulunut aika: 11.56071424484253
#   Kyselyn suoritukseen kulunut aika: 1.2716236114501953
#   Ohjelman suorittamiseen kulunut aika kun kyselyitä tehostavat indeksit on lisätty ennen kyselyitten suorittamista: 12.873228549957275