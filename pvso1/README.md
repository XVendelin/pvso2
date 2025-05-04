# Popis funkcie skriptu
## Inicializácia kamery
  Skript nájde a otvorí prvú pripojenú XIMEA kameru, nastaví expozíciu a aktivuje automatické vyváženie bielej.

## Zber obrázkov
  Postupne zaznamená 4 snímky po stlačení medzerníka a uloží ich ako img1.jpg až img4.jpg.

## Vytvorenie mozaiky
  Zachytené obrázky sa zlúčia do jednej mozaiky vo formáte 2x2 a uložia ako M.jpg.

## Filtrovanie
  Na mozaiku sa aplikuje jednoduchý Laplace-filter, výsledok sa uloží ako M_2.jpg.

## Otáčanie obrázka
  Časť mozaiky sa otočí o 90° a výsledok sa uloží ako M_3.jpg.

## Zachovanie iba červenej zložky
  V spodnej ľavej časti obrázka sa zachová iba červený kanál a uloží sa ako M_4.jpg.

## Výpis informácií
  Na konci sa zobrazí typ dát, rozmery a veľkosť výsledného poľa.

## Ukončenie
  Program čaká na stlačenie klávesy q a následne ukončí zber a zobrazovanie obrázkov.