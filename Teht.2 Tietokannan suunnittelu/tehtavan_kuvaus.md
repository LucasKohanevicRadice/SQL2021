Tehtävä 2: Tietokannan suunnittelu

Tehtävänanto löytyy osoitteesta: https://tasks.withmooc.fi/tikape-kesa-2021/2

Alla on kirjalliset vastaukset, jota tehtävänannossa pyydettiin.


SQL-skeema

Kirjoita tähän CREATE TABLE -komennot, jotka määrittelevät tietokannan.

CREATE TABLE Kayttaja {
id INTEGER PRIMARY KEY,
nimi VARCHAR
salasana VARCHAR   };

CREATE TABLE Video {
id INTEGER PRIMARY KEY,
nimi VARCHAR,
videon_data DATA,
kayttaja_id INT REFERENCES Kayttaja,
yla_peukku INT,
ala_peukku INT,
upload_time DATETIME,

};

CREATE TABLE Videon_kuvaus {
id INTEGER PRIMARY KEY,
video_id INTEGER REFERENCES Video,
avainsana1 VARCHAR,
avainsana2 VARCHAR,
avainsana3 VARCHAR,
avainsana4 VARCHAR,
avainsana5 VARCHAR,

};

CREATE TABLE Videon_arvostelu {
id INTEGER PRIMARY KEY,
video_id INT REFERENCES Video,
arvostelija_id INT REFERENCES Kayttaja,
arvio null // True on peukku ylös, False on peukku alas. Kun arvostelu annetaan, joko ylä - tai alapeukku laskuriin lisätään yksi peukku lisää. Tämä estää useamman äänen antamisen};


CREATE TABLE Kommentin_arvostelu {
id INTEGER PRIMARY KEY,
video_id INTEGER REFERENCES Video,
lahettaja_id INT REFERENCES Kayttaja,
kommentti_id INT REFERENCES Videon_kommentti,
arvio null // Tässäkiin True = peukku ylös ja False = peukku alas

};

CREATE TABLE Tilaajat {
id INT PRIMARY KEY,
kayttaja_id INT REFERENCES Kayttaja,
tilaaja_id INT REFERENCES Kayttaja,
tilaus_aika DATETIME[NOW]
};

CREATE TABLE TILAUKSET {
id INTEGER PRIMARY KEY,
kayttaja_id INTEGER REFERENCES Kayttaja,
tilattava_id INTEGER REFERENCES Kayttaja,
tilaus_aika DATETIME [NOW]
};

CREATE TABLE Kanava {
id INTEGER PRIMARY KEY,
kayttaja_id INT REFERENCES Kayttaja,
video_id INT REFERENCES Video,
nimi VARCHAR
};

CREATE TABLE Soittolista {
id INT PRIMARY KEY
video_id INT REFERENCES VIDEO,
kayttaja_id INT REFERENCES Kayttaja,
soittolista_nimi VARCHAR
};

CREATE TABLE ystavalista {
id INT PRIMARY KEY,
kayttaja1_id INT REFERENCES Kayttaja
kayttaja2_id INT REFERENCES Kayttaja
kayttaja1_lupa TRUE
kayttaja2_lupa TRUE
// Käyttäjät eivät ole oletusarvoisesti toistensa estolistoilla
//Jos lupa muutetaan Falseksi kumman tahansa osalta, niin kyvykkyys lähettää viestejä estetään molemmin puolin back endin puolella.
};

CREATE TABLE Yksityisviestit {
id INTEGER PRIMARY KEY,
kayttaja1_id INTEGER REFERENCES Kayttaja
kayttaja2_id INTEGER REFERENCES Kayttaja
lahetetyt varchar
saapuneet varchar
};

CREATE TABLE Tekstitykset {
id INT PRIMARY KEY,
video_id INT REFERENCES Video,
teksti varchar
aika timestamp
};



Tietokantakaavio

Tee tietokantakaavio netissä olevalla työkalulla dbdiagram.io ja kirjoita tähän tekstimuotoinen kuvaus, joka määrittelee tietokannan työkalussa.

//// -- LEVEL 1
//// -- Tables and References

// Creating tables
Table Kayttaja {
  id int [pk, increment] // auto-increment
  nimi varchar
  salasana varchar
}

Table Video {
  id int [pk, increment]
  nimi varchar
  videon_data data
  kayttaja_id int
  yla_peukku int 
  ala_peukku int
  upload_time datetime
  
 }

Table Videon_kuvaus {
  id int [pk, increment]
  video_id int 
  avainsana1 varchar
  avainsana2 varchar
  avainsana3 varchar
  avainsana4 varchar
  avainsana5 varchar
}

Table Videon_arvostelu {
  id int [pk, increment]
  video_id int 
  arvostelija_id int
  arvio null // True on peukku ylös, False on peukku alas 
  
  
}


Table Videon_kommentti {
  
  id int [pk,increment]
  video_id int
  kayttaja_id int
  lahettaja_id int
  kommentti varchar
  yla_peukku int
  ala_peukku int
  aika datetime
  
}


Table Kommentin_arvostelu {
  id int [pk, increment]
  
  video_id int 

  lahettaja_id int
  kommentti_id int
  arvio null // True on peukku ylös, False on peukku alas 
  
  
}

Table Tilaajat {
  
  id int [pk,increment]
  
  kayttaja_id int
  tilaaja_id  int
  tilaaja_nimi  varchar
  tilaus_aika  datetime[now]
  
}

Table Tilaukset{
  
  id int [pk,increment]
  
  kayttaja_id int
  tilattava_id int
  tilaus_aika datetime[now]
  
  
}

Table Kanava {

  id int [pk, increment]
  kayttaja_id int
  video_id int
  
  nimi varchar
  
}

Table Soittolista {
  id int [pk,increment]
  
  video_id int
  kayttaja_id int
  
  soittolista_nimi varchar
  
}


Table Ystavalista {
  
  id int [pk,increment]
  
  kayttaja1_id int
  kayttaja2_id int
  
  kayttaja1_lupa True 
  kayttaja2_lupa True 
  // Kayttajat eivät ole oletusarvoisesti toistensa estolistoilla.
  // Jos lupa muutetaan Falseksi, kyvykkyys lähettää viestejä 
  // käyttäjien välillä,  estetään back endin puolella.
  
  
}

Table Yksityisviestit {

  id int [pk,increment]
  
  kayttaja1_id int
  kayttaja2_id int
  
  
  lahetetyt varchar
  saapuneet varchar
  
  
  
  
}

Table Tekstitykset {

  id int [pk,increment]
  
  video_id int
  
  teksti varchar
  aika timestamp
  
}


// Creating references
// You can also define relaionship separately
// > many-to-one; < one-to-many; - one-to-one
Ref: Kayttaja.id > Video.kayttaja_id  
Ref: Video.id > Videon_kuvaus.video_id

Ref: Videon_arvostelu.video_id > Video.id
Ref: Videon_arvostelu.arvostelija_id > Kayttaja.id

Ref: Videon_kommentti.video_id - Video.id
Ref: Videon_kommentti.lahettaja_id - Kayttaja.id

Ref: Kommentin_arvostelu.video_id - Video.id

Ref: Kommentin_arvostelu.kommentti_id - Videon_kommentti.id

Ref: Kanava.kayttaja_id - Kayttaja.id
REF: Kanava.video_id - Video.id

Ref: Soittolista.video_id - Video.id
Ref: Soittolista.kayttaja_id - Kayttaja.id

Ref: Tilaukset.kayttaja_id - Kayttaja.id
Ref: Tilaukset.tilattava_id - Kayttaja.id

Ref: Tilaajat.tilaaja_id - Kayttaja.id
Ref: Tilaajat.kayttaja_id - Kayttaja.id

Ref: Ystavalista.kayttaja1_id - Kayttaja.id
Ref: Ystavalista.kayttaja2_id - Kayttaja.id

Ref: Yksityisviestit.kayttaja1_id - Kayttaja.id
Ref: Yksityisviestit.kayttaja2_id - Kayttaja.id


Vaatimusten toteutus

Kuvaa tässä, miten mikäkin vaatimus voidaan toteuttaa tietokantasi avulla. Anna lyhyt sanallinen kuvaus sekä hahmotelma asiaan liittyvistä SQL-komennoista.


Miten vaatimus 1 toteutetaan?

Videota tallennettaessa sivustolle videon nimi, sisältö, julkaisupvm ja videon luoja tallentuvat Video tauluun.  Videon kuvaukseen on mahdollista asettaa 5 erilaista avainsanaa, jotka määrittelevät Videon ydinsisällön. Videon_kuvaus taulu on linkitettynä Video tauluun, joten oikeilla avainsanoilla löytyy oikeat videot.

INSERT INTO Video (nimi, videon_data, kayttaja_id, upload_time) VALUES (x,y.mp4,a,e)


Miten vaatimus 2 toteutetaan?

Videon arvostelu onnistuu siten, että jokaisella videon katsojalla on mahdollisuus tallettaa boolean arvo videolla. Jos käyttäjä painaa front endissä yläpeukkua, tallettuu tietokantaan käyttäjältä tieto TRUE linkitettynä videoon, jos taas käyttäjä painaa alapeukkua, tallettuu tieto False. Jokainen TRUE ja FALSE arvo tallennetaan Video taulukossa oleviin ylä_peukku ja ala_peukku laskureihin.

Esim. yhdessä back endin kanssa: 
IF ylä_peukku: 

UPDATE Videon_arvostelu SET arvio=TRUE WHERE Video.id = Videon_arvostelu.video_id
UPDATE Video SET yla_peukku = yla_peukku+1 WHERE Video.id = Videon_arvostelu.video_id AND arvio = TRUE

ELIF ala_peukku:

UPDATE Videon_arvostelu SET arvio=False WHERE Video.id = Videon_arvostelu.video_id
UPDATE Video SET ala_peukku = ala_peukku+1 WHERE Video.id = Videon_arvostelu.video_id AND arvio = FALSE


Miten vaatimus 3 toteutetaan?


Katselijamäärä saadaan selvitettyä ja tuotua esiin tallentamalla jokaisen katselukerran yhteydessä katselijan id ja videon id Katselija taulukkoon, joka on linkitettynä Video taulukkoon. 

esim. Katselukerrat

SELECT COUNT(Katselija.katselija_id)

FROM Video, Katselija

WHERE Video.id = Katselija.video_id and video.id = xy

esim. peukut

SELECT yla_peukku, ala_peukku 
FROM Video
WHERE Video.id = xy


Miten vaatimus 4 toteutetaan?


Videon kommentit tallennetaan Videon_kommentti Taulukkoon, joka on linkitetty Video, Kayttaja (videon luoja), Kayttaja (kommentin lahettaja) tauluihin.

Front endin puolella on kommenttilaatikko, josta kommentti tallennetaan Videon_kommentti.kommentti sarakkeeseen. Samaan aikaan tallentuvat videon_id ja lähettäjän_id. Videon luojan id tallennetaan myös tideonhaun helpottamista varten. Kun kommentti luodaan, kommenttiin tulevat myös yla- ja ala_peukku laskurit. Ne toimivat samalla tavalla kuin videon arvostelu. True = yläpeukku, False = alapeukku jne.

Kommentin arvostelu tapahtuu Kommentin_arvostelu taulukon kautta, joka on linkitetty Video tauluun, Videon_kommentti tauluun ja Kayttaja tauluun. Video_id avulla löydetään oikea video, kommentti_id avulla oikea kommentti, arvostelija id tallentaa arvostelijan.ideen tietokantaan ja arvio luo True/False tiedon videon arvostelusta.

esim.

yla_peukku:

UPDATE Kommentin_arvostelu SET arvio = TRUE WHERE Videon_kommentti.id = Kommentin_arvostelu.kommentti_id
UPDATE Videon_kommentti SET yla_peukku = yla_peukku + 1 WHERE Videon_kommentti.id = Kommentin_Arvostelu.kommentti_id

ala_peukku:
UPDATE Kommentin_arvostelu SET arvio = FALSE WHERE Videon_kommentti.id = Kommentin_arvostelu.kommentti_id
UPDATE Videon_kommentti SET ala_peukku = ala_peukku + 1 WHERE Videon_kommentti.id = Kommentin_Arvostelu.kommentti_id


Miten vaatimus 5 toteutetaan?

Kanava taulukossa on viittaus Video taulukkoon, video_id:n kautta. Tätä kautta saadaan kaikki haluama data ja informaatio haluamasta videosta liitettyä kanavaan. Video taulukossa on siis tallennetteu kaikki videot kayttajalle tallennetut videot datoineen. Jos kayttaja haluaa lisätä videon kanavalleen, käyttäjälle annetaan toiminto, jossa hän voi valita haluamansa videon, jonka lisätä, josta jää tällöin Kanava taulukosta video_id linkki Video taulukon id:hen, josta kaivetaan kaikki muu data ulos. Tällä vältetään datan tallentamista turhaan useampaan paikkaan, kun säilytetään pelkkä viite alkuperäiseen lähteeseen.

Esim. Back end kielen (ja front endin) kanssa voisi toimia seuraavanlaisella idealla:

IF lisaa_video():

input("Valitse lisättävä video: ")

*Valitsee videon

INSERT INTO Kanava(video_id, kayttaja_id, video_nimi) VALUES ('Video.id, Kayttaja.id, Video.nimi')
FROM Video

Kun katsoja haluaa katsoa videota tuodaan esille:

SELECT Video.data, Video.nimi, Video.upload_time, jnejne FROM Video, Kanava WHERE Kanava.video_id = Video.id

Ylemmässä esimerkissä tottakai data ja informaatio jaotellaan eri kohtiin näyttöä ja sivustoa. 


Miten vaatimus 6 toteutetaan?


Soittolista toteutetaan täysin samalla tavalla kuin kanava (Vaatimus 5). Soittolista on kuin "mini" kanava. Soittolistaan talletetaan video_id viitteet alkuperäisestä datasta, ja soittolistaan tallennetaan vain ne viitteet niihin videoihin jotka halutaan tallentaa soittolistalle.


Esim. Back end kielen (ja front endin) kanssa voisi toimia seuraavanlaisella idealla:

IF lisaa_video():

input("Valitse lisättävä video: ")

*Valitsee videon

INSERT INTO Soittolista(video_id, kayttaja_id, video_nimi) VALUES ('Video.id, Kayttaja.id, Video.nimi')
FROM Video

Kun katsoja haluaa katsoa videota tuodaan esille:

SELECT Video.data, Video.nimi, Video.upload_time, jnejne FROM Video, Soittolista WHERE Soittolista.video_id = Video.id

Ylemmässä esimerkissä tottakai data ja informaatio jaotellaan eri kohtiin näyttöä ja sivustoa. 



Miten vaatimus 7 toteutetaan?


Kun käyttäjä tilaa toisen käyttäjän kanavan, tästä tallentuu tilaajan, tilattavan kayttaja_id:t, sekä tilaus_aika ja tilattavan kanava_id.

Tällöin rakennettaisiin back endin puolelle funktio, jossa aina kun tilattavan kanavaan tulisi lisäyksiä, lähettäisi tämä funktio ilmoituksen kaikille tilattavan seuraajille.

Back endissä voisi olla esimerkiksi lista, jossa on tieto tilatun kanavan senhetkisistä videoista, ja aina kun kanavaan lisätään videoita niin tämä lista päivittyy ja siitä lähetetään ilmoitus tilaajalle.

esim.

SELECT COUNT(Kanava.video_id)

FROM Kanava, Video

WHERE Kanava.video_id = Video.id


Miten vaatimus 8 toteutetaan?


Tilaajat taulukossa on tilaus_aika pylväs. Tämän avulla voidaan jaotella informaatio siten, että nähdään milloin kukin käyttäjä on tilannut minkäkin kanavan. Tästä on myös helppo luoda back endin funktio, joka käyttäisi esimerkiksi SQL:n COUNT funktiota ja tilaus_aika pylvästä hyväkseen, luodakseen joka päivälle oman sivun.

Videon katselukertojen laskeminen toimii hieman eri tavalla. Videoitten katseluun on luotu oma Katselija taulukko. Aina kun videota katsotaan, tallennetaan taulukkoon katselija_id, video_id ja katselu_aika.
Tästä voidaan luoda funktio, jossa myös COUNT funktiolla lasketaan ja tuodaan esiin videon katselukerrat. Katselu_aika pylvään takia, voidaan myös tarkastella katselukertoja eri aikoina.


esim.

SELECT COUNT (Tilaajat.tilaaja_id)
FROM Tilaajat
WHERE Tilaajat.tilaus_aika = xx.yy.eee



Miten vaatimus 9 toteutetaan?


Oletusarvoisesti tällä nettisivulla kaikki ovat "ystäviä", kunnes toisin määrätään estämisen kautta. 
Taulukossa Ystävälista on kahden henkilön käyttäjä_id:t. Jos kumpi tahansa käyttäjistä päättää estää toisen, muutetaan kayttajaX_lupa Falseksi ja täten kumpikaan ei ole enään kykeneväinen lähettämään toiselle viestejä.

esim. 

if esto()

UPDATE Ystavalista SET kayttaja1_lupa = False

WHERE Kayttaja1_id = xxx AND Kayttaja2_id = yyy

Jos ei estoa ja halutaan lähettää/vastaanottaa viestejä:

lähetys:
INSERT INTO Yksityisviestit (lahetetyt) VALUES ('morjenttes')
WHERE Kayttaja.kayttaja1_id = xxx AND Kayttaja.kayttaja2_id = yyy

samaan aikaan käyttäjä2:

INSERT INTO Yksityisviestit (saapuneet) VALUES ('morjenttes')

WHERE Kayttaja.kayttaja1_id = xxx AND Kayttaja.kayttaja2_id = yyy




Miten vaatimus 10 toteutetaan?


Tekstityksille on luotu oma taulukko, jossa on video_id, teksti pylväs, johon tallennetaan haluttu tekstitys ja aika_alku ja aika_loppu pylväs, johon merkataan haluttu aika, jolloin tekstiä haluttaisiin esitettävän. Tämän toiminnallisuuden toteuttaminen vaatisi kuitenkin front endin osaamista, jota ei vielä ole opetettu. 

esim.

SELECT teksti, aika_alku, aika_loppu
FROM Tekstitykset
WHERE video_id = Video.id