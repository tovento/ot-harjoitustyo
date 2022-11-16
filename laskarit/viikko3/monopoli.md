```mermaid
 classDiagram
      Pelaaja "1" -- "1" Nappula
      Nappula "*" -- "1" Ruutu
      Ruutu "40" -- "1" Pelilauta
      Pelaaja ..> Noppa
      Pelaaja "2..4" -- "1" Pelilauta
```
