# Lukupäiväkirja
**Ohjelmistotekniikka, syksy 2022**

Lukupäiväkirjan avulla käyttäjä voi kirjata muistiin tietoja lukemistaan kirjoista sekä pitää listaa kirjoista, jotka haluaa lukea. Sovelluksen kehitys edistyy viikoittain loppusyksyllä 2022.

## Uusin release

Uusin release löytyy
[täältä](https://github.com/tovento/ot-harjoitustyo/releases).

## Asennus ja käyttöönotto

Sovellus on kehitetty ja testattu Python-versiolla 3.10. On mahdollista, että sovellus ei toimi tarkoituksenmukaisesti vanhemmilla Pythonin versioilla.

Sovelluksen käyttö vaatii [Poetryn](https://python-poetry.org/) asennuksen.

Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
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
