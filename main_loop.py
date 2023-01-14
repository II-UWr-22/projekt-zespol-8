################################################
# Głowna pętla - to tutaj toczy się gra        #
################################################

from game_functions import place_pawn, choose_pawn, check_for_win
from board import Piece, Board


#Prowizoryczny ekran startowy

startowa_wiadomość = """
\t\tMenu:

\t[1] Rozpocznij grę 

\t[2] Wyświetl zasady 

\t[3] Wyjście 
"""


def gra():          #Tutaj jest rozgrywka
    print("\n" * 100)
    board = Board()

    print('\n\n\n[Menu] by zakończyć rozgrywkę w dowolnym momencie wpisz\n\n')

    gracz = 0       #O to gracz pierwszy, a 1 to gracz drugi

    while len(board.available_pieces)  > 0:                             #Tutaj zostanie dodany warunek zwycięstwa gdy zostanie zaimplementowany logicznie
        print(board)

        print('Dostępne pionki: ')
        lista_pionków = [Piece(x) for x in board.available_pieces]      #Lista pionków 
        for pionek in lista_pionków:                                    #Wyświetla dostępne pionki wraz z atrybutami
            print(pionek)
        print('\n\n')

        print(f"\t\tRuch gracza {gracz + 1}")                           #Wybiera pionek drugiemu graczowi
        pawn = choose_pawn(board)
        if pawn == 'Menu':
            break
        print("\n")

        print(f"\t\tRuch gracza {2 -gracz}")                            #Wybiera gdzie kładzie zadany pionek
        pomoc = place_pawn(board,pawn)      # Pola od 00 do 33
        if pomoc == "Menu":
            break
        if check_for_win():
            return 2 -gracz  #zwraca numer gracza który stawiał pionka

        gracz = (gracz+1)%2
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
    input(treść)


def wygrana(gracz):
    if gracz:
        print(f"Wygrywa gracz {gracz}")
    else:
        print("Remis")


while True:     #Tutaj jest menu                

    while True:
        wybór_startowy = input(startowa_wiadomość)
        if wybór_startowy not in ['1','2','3']:               #Nasze opcje w menu (jak ktoś ma propozycje to proszę pisać)
            print('[Taka opcja nie istnieje]\n\n')
        else:
            wybór_startowy = int(wybór_startowy)
            break

    if wybór_startowy == 1:
        wygrany = gra()
        wygrana(wygrany)
    elif wybór_startowy == 2:
        zasady()
    elif wybór_startowy == 3:
        break

print('Dziękujemy za grę :D')


#TODO
# 1. Funkcja sprawdzająca czy ktoś już wygrał
# 2. Jakiś output planszy, żeby było widać co to za pionki
# 3. Zakończenie gry (informacja o wyniku rozgrywki i powrót do menu)



