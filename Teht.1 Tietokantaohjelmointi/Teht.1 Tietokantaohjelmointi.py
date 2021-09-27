import sqlite3
import time

# start = time.time()


db = sqlite3.connect("kurssit.db")
db.isolation_level = None



def op_yht_maara_vuonna(vuosi: str):

    opintopisteet_yht = 0


    opintopisteet = db.execute(f"SELECT Kurssit.laajuus FROM Kurssit,Suoritukset WHERE Suoritukset.kurssi_id = Kurssit.id AND Suoritukset.paivays LIKE '%{vuosi}%'").fetchall()

    for rivi in opintopisteet:

        opintopisteet_yht += int(rivi[0])
    
    if opintopisteet_yht == 0:
        return f"Vuodelta {vuosi} ei löytynyt yhtään suorituksia"

    else:
        return opintopisteet_yht
        



#   Runneth thy pockets, you scallywag!




def opiskelijan_suoritukset_jarjestyksessa(opiskelija: str):

    k_ja_l = db.execute(f"SELECT Kurssit.nimi, Kurssit.laajuus, Suoritukset.paivays, Suoritukset.arvosana FROM Kurssit,Suoritukset,Opiskelijat WHERE Opiskelijat.nimi = '{opiskelija}' AND Opiskelijat.id = Suoritukset.opiskelija_id AND Suoritukset.kurssi_id = Kurssit.id ORDER BY Suoritukset.paivays ")

    lista = []

    for rivi in k_ja_l:
        lista.append(rivi)

    if len(lista) == 0:
        print("Annetulla nimella ei löytynyt suorituksia.")
    else:
        print(f"kurssi         op   päiväys        arvosana")

        for rivi in lista:
            print(f"{rivi[0]:12}   {rivi[1]:<2}   {rivi[2]:>2}   {rivi[3]:>3}")




def tulosta_kurssin_arvosana_jakauma(kurssi: str):

    kurssimaara = 0

    data = db.execute(f"SELECT COUNT(Kurssit.nimi) FROM kurssit WHERE Kurssit.nimi = '{kurssi}' ")

    for rivi in data:
        kurssimaara += int(rivi[0])


    ykkoset = db.execute(f"SELECT COUNT(*) FROM Suoritukset, Kurssit WHERE Suoritukset.kurssi_id = Kurssit.id AND Kurssit.nimi = '{kurssi}' AND Suoritukset.arvosana = {1} ")
    kakkoset = db.execute(f"SELECT COUNT(*) FROM Suoritukset, Kurssit WHERE Suoritukset.kurssi_id = Kurssit.id AND Kurssit.nimi = '{kurssi}' AND Suoritukset.arvosana = '2' ")
    kolmoset = db.execute(f"SELECT COUNT(*) FROM Suoritukset, Kurssit WHERE Suoritukset.kurssi_id = Kurssit.id AND Kurssit.nimi = '{kurssi}' AND Suoritukset.arvosana = 3 ")
    neloset =  db.execute(f"SELECT COUNT(*) FROM Suoritukset, Kurssit WHERE Suoritukset.kurssi_id = Kurssit.id AND Kurssit.nimi = '{kurssi}' AND Suoritukset.arvosana = 4 ")
    vitoset =  db.execute(f"SELECT COUNT(*) FROM Suoritukset, Kurssit WHERE Suoritukset.kurssi_id = Kurssit.id AND Kurssit.nimi = '{kurssi}' AND Suoritukset.arvosana = 5  ")

    if kurssimaara == 0:
        print(f"Annetulla kurssikoodilla ei löytynyt kursseja")
    else:
        for rivi in ykkoset:
            print(f"Arvosana 1: {rivi[0]} kpl")
        
        for rivi in kakkoset:
            print(f"Arvosana 2: {rivi[0]} kpl")

        for rivi in kolmoset:
            print(f"Arvosana 3: {rivi[0]} kpl")

        for rivi in neloset:
            print(f"Arvosana 4: {rivi[0]} kpl")

        for rivi in vitoset:
            print(f"Arvosana 5: {rivi[0]} kpl")



def Parhaat_pisteyttäjät(määrä: int):

    opet_ja_opisteet = db.execute(f"SELECT Opettajat.nimi, SUM(Kurssit.laajuus) FROM Kurssit, Opettajat, Suoritukset WHERE kurssit.opettaja_id = Opettajat.id AND Suoritukset.kurssi_id = Kurssit.id GROUP BY Opettajat.nimi ORDER BY SUM(Kurssit.laajuus) DESC ")
    opet_ja_opintopisteet_listana = []
    
    for rivi in opet_ja_opisteet:
        opet_ja_opintopisteet_listana.append(rivi)

    print(f"Opettaja             op")

    for i in range(0, määrä):

        print(f"{opet_ja_opintopisteet_listana[i][0]:21}{opet_ja_opintopisteet_listana[i][1]}")

def tietokantaohjelma():

    while True:

        toiminto = int(input("Valitse toiminto: "))

        if toiminto == 1:

            vuosi = input("Anna vuosi: ")
            print(op_yht_maara_vuonna(vuosi))
        
        elif toiminto == 2:
            opiskelija = input("Anna opiskelijan nimi: ")
            opiskelijan_suoritukset_jarjestyksessa(opiskelija)
        
        elif toiminto == 3:
            kurssi = input("Anna kurssin nimi: ")
            tulosta_kurssin_arvosana_jakauma(kurssi)
        
        elif toiminto == 4:
            maara = int(input("Anna opettajien määrä: "))
            Parhaat_pisteyttäjät(maara)
        
        elif toiminto == 5:
            break


start = time.time()
tietokantaohjelma()
print(f"aikaa kului {time.time() - start}")

#   Ohjelmointikielenä käytettiin pythonia