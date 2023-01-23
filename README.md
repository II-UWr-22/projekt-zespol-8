# Projekt z PWI zespołu 8 - implementacja gry Quarto

## Zasady gry

Gra jest przeznaczona dla 2 graczy. \
Do gry służą plansza 4x4 i 16 pionków, które posiadają 4 różne atrybuty (kolor, wysokość, kształt i obecność kropki na górze). W każdej turze jedna osoba wybiera dowolny pionek dla drugiej osoby, która ma za zadanie umieścić go w dowolnym miejscu na planszy. W następnej turze ich role się zamieniają. \
Gra kończy się gdy wszystkie pionki zostały umieszczone na planszy lub gdy jeden z graczy osiągnie wygraną. \
Wygraną osiąga gracz, który postawi pionek, dzięki któremu na planszy powstanie rząd pionków z conajmniej jednym wspólnym atrybutem. Rząd może być w pionie, poziomie lub po skosie.

## Wymagania systemowe

- Python 3.10 \
Sprawdzić wersję Pythona można poleceniem ```python -V``` \
Najnowszą wersję Pythona można zainstalować poleceniem ```sudo apt-get install python3```

- biblioteka Turtle do Pythona \
Sprawdzić czy jest zainstalowana można poleceniem: ```python3 -m pip show PythonTurtle``` \
Można ją zainstalować poleceniami: \
```sudo apt install python3-pip``` \
```sudo pip3 install PythonTurtle```

## Uruchamianie

Żeby uruchomić grę należy sklonować repozytorium na swój dysk, następnie wejść do folderu, do którego ono zostało sklonowane i uruchomić plik main_loop.py w interpreterze pyhtona, co z konsoli można zrobić  poleceniem ```python3 main_loop.py```

## Autorzy

- Anna Pierzchała
- Viktor Grünwaldt
- Antoni Strasz
- Kacper Pajor
- Bartosz Marchewka
- Dominik Walecko
