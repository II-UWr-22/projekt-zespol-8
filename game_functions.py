from turtle import *


# Wybiera pionka po id, usuwa go z dostępnych i zwraca id
def choose_pawn(board):
    while True:
        
        pawn = textinput("Pionek", "Podaj pionka, którego ma postawić twój przeciwnik: ")          #Drobna zmiana, żeby [Menu] przerywało rozgrywkę
        try:
            pawn = int(pawn)
        except:
            if pawn.strip().lower() == 'menu':
                return 'Menu'
            print("Pionek musi być liczbą")
            continue
        if pawn in board.available_pieces:
            board.available_pieces.remove(pawn)
            break
        else:
            print("Zły pionek")
    return pawn


# Kładzie pionka na wybranym polu
def place_pawn(board, pawn):
    while True:
        position = textinput("Pole", f"Podaj pole (|00| - |33|) na które chcesz postawić pionka {pawn}: ")
        if position.strip().lower() == "menu":                                      #Kolejna zmiana umożliwiająca przerwanie gry
            return "Menu"
        try:
            x,y = int(position[0]),int(position[1])
            if not board.board[x][y]:
                board.set_piece(x, y, pawn)
                return (x, y)                                                       #Lokacja piąka pozwala na dostanie jego atrybutów
            else:
                print("Pozycja zajęta")
        except:
            print("Podaj poprawną pozycję")


def check_for_win(board, pawn_location):
        x, y = pawn_location[0], pawn_location[1]
        attributes = board.board[x][y].attributes
        for atr in attributes:
            if check_diag(atr, x, y, board):
                return True
            if check_hori(atr, x, y, board):
                return True
            if check_vert(atr, x, y, board):
                return True
        return False

def check_hori(atr, x, y, board):
    for i in range(0 - y, 4 - y):
        piece = board.board[x][y + i]
        if piece == None or atr not in piece.attributes:
            return False
    return True
def check_vert(atr, x, y, board):
    for i in range(0 - x, 4 - x):
        piece = board.board[x + i][y]
        if piece == None or atr not in piece.attributes:
            return False
    return True
def check_diag(atr, x, y, board):
    L = [(i, i) for i in range(4)]
    P = [(i, 3 - i) for i in range(4)]
    if (x, y) in L:
        for i in L:
            piece = board.board[i[0]][i[1]]
            if piece == None or atr not in piece.attributes:
               return False
        return True
    elif (x, y) in P:
        for i in P:
            piece = board.board[i[0]][i[1]]
            if piece == None or atr not in piece.attributes:
                return False
        return True
    return False


# rysowanie pionkow na planszy
def move(x, y):
    penup()
    goto(x, y)
    pendown()


def draw_square(side, colour, x, y):
    move(x, y)
    fillcolor(colour)
    begin_fill()
    penup()
    lt(90)
    fd(side / 2)
    rt(90)
    pendown()
    fd(side / 2)
    for x in range(3):
        rt(90)
        fd(side)
    rt(90)
    fd(side / 2)
    end_fill()


def draw_circle(side, colour, x, y):
    move(x, y)
    fillcolor(colour)
    begin_fill()
    penup()
    lt(90)
    fd(side / 2)
    lt(90)
    pendown()
    circle(side / 2)
    end_fill()


# zwraca wspolrzedna pionka w zaleznosci od jego pozycji (0,1,2,3) i dl. kratki
def ret_x(x, length):
    if x == 0:
        x = (x - 2) * length * 3 / 2
    if x == 1:
        x = (x - 2) * length
    if x == 2:
        x = (x - 1) * length
    if x == 3:
        x = (x - 1) * length * 3 / 2
    return x


def draw_pawn(x, y, side, board):  # side to dlugosc boku/srednicy pionka, xy to wspolrzedne jego srodka
    tracer(0, 1)
    length = side * 5 / 4 / 2   # length to odleglosc srodka pionka od kratki boarda. Pierwsze dwie liczby okreslaja stosunek kratki boarda do wielkosci pionka.
    colour = board.board[x][y].attributes[0]
    height = board.board[x][y].attributes[1]
    shape1 = board.board[x][y].attributes[2]
    dot1 = board.board[x][y].attributes[3]
    x = ret_x(x, length)
    y = ret_x(y, length)
    move(x, y)

    if height == "short":
        side /= 2

    if colour == "dark":
        colour = "black"
    else:
        colour = "grey"

    if shape1 == "square":
        draw_square(side, colour, x, y)
        if dot1 == "has dot":
            move(x, y)
            draw_square(side / 3, "white", x, y)
    else:
        draw_circle(side, colour, x, y)
        if dot1 == "has dot":
            move(x, y)
            draw_circle(side / 3, "white", x, y)
    update()