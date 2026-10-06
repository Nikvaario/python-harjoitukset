# Ohjelmisto 1 - Peliprojekti

**Niko Rahikainen**

Peliprojektini ideana on tehdä roskien keräämiseen sekä kierrätykseen liittyvä seikkailupeli, jossa pelaaja seikkailee syrjäseutuisella kaupungilla. 
Pelaajan tavoitteena on selvitä kaupungin puistosta kaupungintalolle eri kaupungin kohteiden läpi, samalla keräten määrätyn määrän roskia sekä ylittää mielenkiintoisia esteitä käyttäen keräämiä roskia. 

Kestävän kehityksen tavoitteissa peli keskittyy seuraaviin: 12. Vastuullista kuluttamista, 13. Ilmastotekoja sekä 15. Maanpäällinen elämä

# Projektirakenne

- Moduulit
- gameproject.py #Pääohjelma
- README.md

# Projektitehtävien dokumentointi

## Projekti 1
Tein peliprojektin ensimmäisen osion 21.8. jolloin lisäsin ohjelmaan pelaajan nimen sekä iän kysymisen, jonka jälkeen ohjelma kutsuu pelaajan tervetulleeksi ja avaa pienen stats näkymän, jossa lukee pelaajan nimi ja ikä.

## Projekti 2
Tein peliprojektin toisen osion 3.9. jolloin lisäsin ohjelmaan ikätarkistuksen, joka pysäyttää ohjelman mikäli käyttäjä ilmoittaa iäkseen 12. Importtasin tätä varten sys moduulin, jonka kautta voi näppärästi käyttää sys.exit() komentoa lopettamaan ohjelman.

Tein myös erilaisia komentoja käyttäjälle, jonka avulla hän saa lisätietoa pelaajasta sekä ympäristöstä:
-| Inventory: Kertoo mitä tarvikkeita pelaajalla on.
-| Check cash: Kertoo tarkemmin pelaajan käteistilanteen eri kolikkojen määrässä.
-| Surrounding: Kertoo pelaajan nykyisen ympäristön.

Komentoja varten lisäsin stats valikkoon yksinkertaisen cash osion sekä kuvauksen pelaajan inventoryn käytön määrästä.

## Projekti 3
Tein peliprojektin kolmannen osion 8.9. jolloin vaihdoin suurimmanosan koodin osista omiin funktiohin, kuten komentojen kysymisen tai pelaajan tilastojen printtaamisen. Tämän lisäksi loin listan "inventory" jolle on kaksi komentoa: Inventoryn tarkistus sekä tavaran lisääminen sinne. Inventoryn jatkoa ajatellen loin myös muuttujan, jota käytetään maksimikoon merkkaamiseen.

Ohjelmasta poistumista varten loin myös varmistusta varten funktion, joka kysyy "Cancel" komennon antaessa varmistuksen haluaako pelaaja poistua pelistä vai ei.

## Projekti 4

Tein peliprojektin neljännen osion 29.9-2.10 välisenä aikana. 29.9 viimestelin pelin idean, tavoitteen sekä kestävän kehityksen tavoitteet. Kirjoitin nämä tämän tiedoston ylimmäksi tekstiksi ennen "Projektirakenne" osiosta.

2.10 Lisäsin ohjelmaan luokat Player, Trash sekä Area, ja näistä pelille oleelliset oliot. luokka/oliot "Trash" toimii tehtävänannon "esine" pyyntönä ja "Area" tass "huone" pyyntönä. Uudet nimet kuvaavat paremmin oman ideani tarpeita. 
Lisäsin pelille uuden komennenon "Move", jonka avulla pelaaja voi liikkua eteenpäin alueita, kunnes hän saapuu nykyiseen viimeiseen alueeseen. Muokkasin myös "Surrounding" komentoa, jonka kautta pelaaja löytää eri alueilta eri esineitä, joita hän voi kerätä reppuunsa.

Poistin edellisistä projektitehtävistä tulleita komentoja tai funktiota, kuten "Add item" ja "Check cash", koska en kokenut niitä enään tarpeelliseksi peliäni varten.

## Projekti 5

Tein projektin viidennettä osiota 5-6.10 välisenä aikana. 5.10 Loin pelille aloitusmenun, ja sitä vaativat funktiot eri komennoille. Komentoina toimii "N": aloita peli uudella hahmolla, "L": lataa olemassa oleva palaaja, "Q": Lue pelin ohjeteksti sekä "E": poistu pelistä. 

6.10 loin moduulin ./savesystem.py, joka tekee kaiken pelaajan dataan liittyvän tallentamisen sekä lataamisen, kun näitä pyydetään. Pelin edellinen "cancel" komento on muuttunut "exit" komennoksi, ja sensijaan että se kysyy ohjelmasta poistumisen varmistuksen, niin komento kysyy nyt pelaajan datan tallennuksen halua.  

projekti ylitti myös rivimäärän alirajan, eli 200 riviä koodia. 