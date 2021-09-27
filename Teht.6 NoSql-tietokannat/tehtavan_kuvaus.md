Tehtävä 6: NoSQL-tietokannat

Tehtävämateriaali löytyy osoitteesta:   https://tasks.withmooc.fi/tikape-kesa-2021/6

Alla on tehtävänanto ja vastaukseni tehtäviin kopioituna:



Jokaisessa osatehtävässä käännä annetut SQL-komennot MongoDB-kielelle. Varmista MongoDB-tulkin avulla, että komentosi toimivat. Saat kaikista osatehtävistä 2 pistettä paitsi viimeisestä osatehtävästä 3 pistettä.

1. Tiedon lisääminen
sqlite> CREATE TABLE Tyontekijat (id INTEGER PRIMARY KEY, nimi TEXT, yritys TEXT, palkka INTEGER);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Maija', 'Google', 8000);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Uolevi', 'Amazon', 5000);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Kotivalo', 'Google', 7000);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Kaaleppi', 'Facebook', 6000);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Liisa', 'Amazon', 9000);
sqlite> INSERT INTO Tyontekijat (nimi, yritys, palkka) VALUES ('Anna', 'Amazon', 6500);
Kirjoita kuusi insertOne-komentoa, jotka lisäävät tiedot kokoelmaan db.tyontekijat. Huomaa, että MongoDB:ssä kokoelmaa ei tarvitse erikseen luoda, vaan se syntyy automaattisesti.

db.tyontekijat.insertOne({nimi: "Maija", yritys: "Google", palkka: 8000})
db.tyontekijat.insertOne({nimi: "Uolevi", yritys: "Amazon", palkka: 5000})
db.tyontekijat.insertOne({nimi: "Kotivalo", yritys: "Google", palkka: 7000})
db.tyontekijat.insertOne({nimi: "Kaaleppi", yritys: "Facebook", palkka: 6000})
db.tyontekijat.insertOne({nimi: "Liisa", yritys: "Amazon", palkka: 9000})
db.tyontekijat.insertOne({nimi: "Anna", yritys: "Amazon", palkka: 6500})

2. Tiedon hakeminen
sqlite> SELECT * FROM Tyontekijat;
id          nimi        yritys      palkka    
----------  ----------  ----------  ----------
1           Maija       Google      8000      
2           Uolevi      Amazon      5000      
3           Kotivalo    Google      7000      
4           Kaaleppi    Facebook    6000      
5           Liisa       Amazon      9000      
6           Anna        Amazon      6500      
Kirjoita find-komento, joka hakee kaiken sisällön kokoelmasta.

db.Tyontekijat.find({})

3. Tiedon muuttaminen
sqlite> UPDATE Tyontekijat SET palkka=5500 WHERE nimi='Uolevi';
sqlite> SELECT * FROM Tyontekijat;
id          nimi        yritys      palkka    
----------  ----------  ----------  ----------
1           Maija       Google      8000      
2           Uolevi      Amazon      5500      
3           Kotivalo    Google      7000      
4           Kaaleppi    Facebook    6000      
5           Liisa       Amazon      9000      
6           Anna        Amazon      6500      
Kirjoita updateOne-komento, joka muuttaa kokoelman sisältöä, ja sen jälkeen taas find-komento.

db.Tyontekijat.updateOne(
{nimi: "Uolevi"},
{$set:{palkka:5500}}
)

db.tyontekijat.find({})

4. Tietojen rajaaminen
sqlite> SELECT nimi, palkka FROM Tyontekijat WHERE yritys='Amazon';
nimi        palkka    
----------  ----------
Uolevi      5500      
Liisa       9000      
Anna        6500      
Kirjoita find-komento, joka hakee nimen ja palkan jokaisesta Amazonin työntekijästä. Komento ei saa hakea muuta tietoa.

db.Tyontekijat.find({Tyontekijat, palkka: {yritys: "Amazon"}})

5. Lukumäärän laskeminen
sqlite> SELECT COUNT(*) FROM Tyontekijat WHERE yritys='Google';
COUNT(*)  
----------
2         
Kirjoita count-komento, joka hakee Googlen työntekijöiden määrän.

db.Tyontekijat.count( {Tyontekijat: {yritys: "Google"}} )

6. Vertailu ehdossa
sqlite> SELECT nimi, yritys FROM Tyontekijat WHERE palkka>6000;
nimi        yritys    
----------  ----------
Maija       Google    
Kotivalo    Google    
Liisa       Amazon    
Anna        Amazon    
Kijoita find-komento, joka hakee niiden työntekijöiden nimen ja yrityksen, joiden palkka on yli 6000.

db.Tyontekijat.find({palkka $gt: 6000})

7. Ryhmittely
sqlite> SELECT yritys, COUNT(*), MAX(palkka) FROM Tyontekijat GROUP BY yritys;
yritys      COUNT(*)    MAX(palkka)
----------  ----------  -----------
Amazon      3           9000       
Facebook    1           6000       
Google      2           8000       
Kirjoita aggregate-komento, joka hakee jokaisen yrityksen työntekijöiden määrän ja työntekijän suurimman palkan.