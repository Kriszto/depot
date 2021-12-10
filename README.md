# Backend Position Házi Feladat

A következő feladatban egy egyszerűsített esemény-vezérelt raktárkezelő rendszer egyik komponensét kell implementálnod. Az egyszerűség kedvéért kétféle eseménnyel kell dolgoznod:

* készletfeltöltés - új készlet érkezik a boltba (event_type: "incoming")
* eladás - a boltban lévő termékből x db-ot eladtak (event_type: "sale")

## A rendszer 2 komponensből fog állni:

* importer: adatok felolvasása, validálása
* Kafka: feldolgozott adatok továbbítása (message bus)

Az importer komponens egy adott mappában CSV fájlokat keres és szerializált formátumban felküldi az `events` nevű Kafka topic-ra. Példa CSV fájlokat csatolva megtalálod.

Néha előfordulhatnak hibás formátumú CSV-k, melyekben egy vagy több érték hiányzik, esetleg bizonyos értékek típusa eltér. Ilyen esetekben az importer logoljon hibát, de indokolatlanul ne haljon meg. Egyetlen sorban szereplő hiba ne vezessen egy egész fájl elvesztéséhez.

## Technikai követelmények

* Az alkalmazáshoz legyen megfelelő teszt suite
* Az alkalmazás legyen elindítható lokálisan konténerizált formában (docker-compose)
* Kérjük ne egy mindentudó frameworkkel (pl.: Django, Rails) készítsd el a megoldást
