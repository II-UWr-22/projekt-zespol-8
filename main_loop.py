################################################
# Głowna pętla - to tutaj toczy się gra        #
################################################

from game_functions import place_pawn, choose_pawn, check_for_win
from board import Piece, Board
from turtle import *
from game_functions import draw_pawn, draw_board, pawn_list

#Prowizoryczny ekran startowy

startowa_wiadomość = """
[1] Rozpocznij grę 

[2] Wyświetl zasady 

[3] Wyjście 
"""


def gra(gracze):          #Tutaj jest rozgrywka
    print("\n" * 100)
    board = Board()

    print('\n\n\n[Menu] by zakończyć rozgrywkę w dowolnym momencie wpisz "Menu"\n\n')

    gracz = 0       #O to gracz pierwszy, a 1 to gracz drugi
    draw_board(0, 0, 50)
    while len(board.available_pieces) > 0:                             #Tutaj zostanie dodany warunek zwycięstwa gdy zostanie zaimplementowany logicznie
        print(board)

        print('Dostępne pionki: ')
        lista_pionków = [Piece(x) for x in board.available_pieces]      #Lista pionków
        light = []  # lista jasnych pionkow
        dark = []  # lista ciemnych pionkow
        for pionek in lista_pionków:  # Wyświetla dostępne pionki wraz z atrybutami
            print(pionek)
            if pionek.attributes[0] == "dark":
                dark.append(pionek)
            else:
                light.append(pionek)
        pawn_list(-500, light, 70)
        pawn_list(500, dark, 70)
        print('\n\n')

        print(f"\t\tRuch gracza {gracze[gracz]}")                           #Wybiera pionek drugiemu graczowi
        pawn = choose_pawn(board, gracze[gracz])
        if pawn == 'Menu':
            break
        print("\n")

        print(f"\t\tRuch gracza {gracze[1 -gracz]}")                            #Wybiera gdzie kładzie zadany pionek
        pomoc = place_pawn(board,pawn, gracze[1 -gracz])      # Pola od 00 do 33
        if pomoc == "Menu":
            break
        draw_pawn(pomoc[0], pomoc[1], 50, board)  # to rysuje pionka na danej pozycji
        if check_for_win(board, pomoc):
            return gracze[1 -gracz]  #zwraca numer gracza który stawiał pionka

        gracz = (gracz+1) % 2
    return None

def zasady():         #To wyświetla zasady
    treść = """
    Gra jest przeznaczona dla 2 graczy. 
    Do gry służą plansza 4x4 i 16 pionków, które posiadają 4 różne atrybuty (kolor, wysokość, kształt i obecność kropki na górze). 
    W każdej turze jedna osoba wybiera dowolny pionek dla drugiej osoby, która ma za zadanie umieścić go w dowolnym miejscu na planszy. W następnej turze ich role się zamieniają. 
    Gra kończy się gdy wszystkie pionki zostały umieszczone na planszy lub gdy jeden z graczy osiągnie wygraną. 
    Wygraną osiąga gracz, który postawi pionek, dzięki któremu na planszy powstanie rząd pionków z conajmniej jednym wspólnym atrybutem. Rząd może być w pionie, poziomie lub po skosie.

    [Enter] Powrót do menu
    """
    textinput("Zasady:", treść)


def wygrana(gracz):
    if gracz:
        textinput("Koniec gry", f"Wygrywa gracz {gracz}")
        clearscreen()
    else:
        textinput("Koniec gry", "Remis")
        clearscreen()

def wczytaj_nazwy_graczy():
    gracz1 = textinput("Gracz nr 1", "Podaj nazwę gracza 1: ")
    gracz2 = textinput("Gracz nr 2", "Podaj nazwę gracza 2: ")
    return (gracz1,gracz2)


while True:     #Tutaj jest menu                

    while True:
        wybór_startowy = textinput("Wybierz opcję", startowa_wiadomość)
        if wybór_startowy not in ['1','2','3']:               #Nasze opcje w menu (jak ktoś ma propozycje to proszę pisać)
            print('[Taka opcja nie istnieje]\n\n')
        else:
            wybór_startowy = int(wybór_startowy)
            break

    if wybór_startowy == 1:
        gracze = wczytaj_nazwy_graczy()
        wygrany = gra(gracze)
        wygrana(wygrany)
    elif wybór_startowy == 2:
        zasady()
    elif wybór_startowy == 3:
        break

print('Dziękujemy za grę :D')
done()



