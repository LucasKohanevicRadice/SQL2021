Tehtävä 4: Transaktioiden toiminta

Tehtävämateriaali löytyy osoitteesta:   https://tasks.withmooc.fi/tikape-kesa-2021/4

Alla on tehtävänanto ja vastaukseni tehtäviin kopioituna:




Jokaisessa seuraavassa testissä lähtökohtana on SQLitessä taulu, joka on luotu seuraavasti:

CREATE TABLE Testi (x INTEGER);
INSERT INTO Testi (x) VALUES (1);

Testissä kuvataan kahdessa transaktiossa tehtävät komennot järjestyksessä. Vasemmalla ovat 1. transaktion komennot ja oikealla 2. transaktion komennot. Testaa komentoja avaamalla kaksi SQLite-tulkkia samaan tietokantatiedostoon.
Tehtäväsi on ilmoittaa, minkä tuloksen SELECT-kyselyt antavat sekä onnistuvatko transaktiot. Transaktio onnistuu, jos kaikki siinä olevat komennot suoritetaan onnistuneesti (eikä tule viestiä Error: database is locked).

Tehtävä muodostuu viidestä testistä. Saat testistä 2 pistettä, jos tulokset ovat oikein ja olet perustellut tulokset. Tehtävästä voi saada yhteensä 10 pistettä.

Testi 1
BEGIN;
SELECT x FROM Testi;
                                   BEGIN;
                                   UPDATE Testi SET x=2;
                                   SELECT x FROM Testi;
                                   COMMIT;
COMMIT;


Minkä tuloksen 1. transaktion SELECT-kysely antaa? 
1
Minkä tuloksen 2. transaktion SELECT-kysely antaa? 
2

Onnistuuko 1. transaktio? 
kyllä

Onnistuuko 2. transaktio? 
ei

Miten perustelet yllä olevat tulokset?

Koska SQlitessä on tason 4 eristys, 1 kyselyyn ei tule muutoksia kesken 1 transaktion, eikä tähän kyseiseen x:n arvoon jota kyselyssä 1 käsitellään voida tehdä muutoksia, koska transaktio 1 on sen varannut.

Testi 2
BEGIN;
SELECT x FROM Testi;
UPDATE Testi SET x=2;
                                   BEGIN;
                                   SELECT x FROM Testi;
                                   COMMIT;
COMMIT;


Minkä tuloksen 1. transaktion SELECT-kysely antaa? 
1
Minkä tuloksen 2. transaktion SELECT-kysely antaa? 
1

Onnistuuko 1. transaktio? 
kyllä

Onnistuuko 2. transaktio? 
kyllä

Miten perustelet yllä olevat tulokset?

1 Transaktio onnisttuu, jopa update komennolla, koska 1 transaktio käynnistettiin ensin.
2 Transaktio onnistuu, koska siinä ei tehdä muutoksia x:n arvoon. Täten se vain hakee x:n arvon ennen 1 transaktion loppuun viemistä.

Testi 3
BEGIN;
UPDATE Testi SET x=2;
                                   BEGIN;
                                   UPDATE Testi SET x=3;
                                   SELECT x FROM Testi;
                                   COMMIT;
SELECT x FROM Testi;
COMMIT;


Minkä tuloksen 1. transaktion SELECT-kysely antaa? 
2
Minkä tuloksen 2. transaktion SELECT-kysely antaa? 
1

Onnistuuko 1. transaktio? 
kyllä

Onnistuuko 2. transaktio? 
ei

Miten perustelet yllä olevat tulokset?

Kuten aiemmassakin testissä, SQlitessä ei voi muuttaa jo toisesssa transaktiossa parhaillaan käsiteltävänä olevaa muuttujan arvoa. Muuttujan arvon voi kyllä noutaa, ajankohdasta, ennen käynnissä olevaa transaktiota, mutta muutoksia siihen ei voi tehdä, eikä päivittynyttä muuttujan arvoa voi noutaa ennenkuin transaktio on valmis.

Testi 4
BEGIN;
UPDATE Testi SET x=2;
                                   BEGIN;
                                   UPDATE Testi SET x=2;
                                   SELECT x FROM Testi;
                                   COMMIT;
SELECT x FROM Testi;
COMMIT;


Minkä tuloksen 1. transaktion SELECT-kysely antaa? 
2
Minkä tuloksen 2. transaktion SELECT-kysely antaa? 
1

Onnistuuko 1. transaktio? 
kyllä

Onnistuuko 2. transaktio? 
ei

Miten perustelet yllä olevat tulokset?

Testi 4 on identtinen testin 3 kanssa, lukuun ottamatta 2 käyttäjän yritystä muuttaa x: arvoa 2:teen, 3:n sijasta. Täten täysin samat perustelut tähän kuin testi 3:seen.

Testi 5
BEGIN;
SELECT x FROM Testi;
                                   BEGIN;
                                   SELECT x FROM Testi;
                                   UPDATE Testi SET x=2;
                                   COMMIT;
UPDATE Testi SET x=3;
COMMIT;


Minkä tuloksen 1. transaktion SELECT-kysely antaa? 
1
Minkä tuloksen 2. transaktion SELECT-kysely antaa? 
1

Onnistuuko 1. transaktio? 
ei

Onnistuuko 2. transaktio? 
ei

Miten perustelet yllä olevat tulokset?

Tässä ilmeisesti käy silleein, että vaikkakin 1 transaktio on ensimmäinen, joka rupee käsittelemään x muuttujaa, 2 transaktiossa ns "varataan" lupa tehdä muutoksia siihen kuitenkin. Joten vaikkakin 1 transaktio käynnistettiin ensin, niin 2 transaktio ns "varasi" luvan tehdä muutoksia ensin UPDATE komennolla.

Tosin ennenkuin 2 transaktioon annettiin uusi commit komento, 1 transaktion commit komennon jälkeen, x:n arvo ei muuttunut globaalisti tietokannassa. Rehellisesti sanottuna hyvin hämmentävä toiminto ja mielestäni jopa omalla tavallaan buginen ominaisuus. Voi tosin olla, etten vain nyt ymmärrä tämän toiminnon käyttötarkoitusta..

