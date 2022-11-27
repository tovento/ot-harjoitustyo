# Lukupäiväkirja
**Ohjelmistotekniikka, syksy 2022**

Lukupäiväkirjan avulla käyttäjä voi kirjata muistiin tietoja lukemistaan kirjoista sekä pitää listaa kirjoista, jotka haluaa lukea. Sovelluksen kehitys edistyy viikoittain loppusyksyllä 2022.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Komentorivitoiminnot

### Ohjelman käynnistäminen

Ohjelma käynnistyy komennolla:
```
poetry run invoke start
```

### Testaus

Testien ajo komennolla:
```
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin generointi komennolla:
```
poetry run invoke coverage-report
```

### Pylint-tarkistus

```
poetry run invoke pylint
```
