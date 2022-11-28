# Changelog

## Viikko 3

- Luotu kaksi alustavaa näkymää käyttöliittymään: lukupäiväkirja ja uuden kirjan
  lisääminen lukupäiväkirjaan. Käyttäjä voi siirtyä näkymästä toiseen. Kirjan
tallentaminen ei vielä onnistu käyttöliittymänäkymän kautta.

- Luotu Book-luokka, joka kuvastaa yhtä lukupäiväkirjaan lisättävää kirjaa.

- Luotu BookJournalService-luokka, joka vastaa sovelluslogiikasta.
- Kirjoitettu testi, joka testaa että Book-luokan objekti välitetään oikein
  BookJournalService-luokkaan.

- Luotu BookJournalRepository-luokka, joka vastaa tietokannan käsittelystä.
- Kirjoitettu kaksi testiä, jotka testaavat:
    - kirjan tallennusta tietokantaan
    - tietokantaan tallennettujen kirjojen hakemista.

## Viikko 4

- Yhdistetty sovellus SQLite-tietokantaan.
- Luettujen kirjojen lisääminen tietokantaan sekä kaikkien luettujen
  kirjojen haku tietokannasta onnistuvat.
- Kehitetty käyttöliittymää:
    - käyttäjä näkee lukemansa kirjat listana sovelluksen etusivulla
    - käyttäjä voi lisätä luettuja kirjoja lukupäiväkirjaan käyttöliittymän
      kautta.
