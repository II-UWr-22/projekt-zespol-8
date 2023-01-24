from turtle import *

# Wybiera pionka po id, usuwa go z dostępnych i zwraca id
def choose_pawn(board, gracz):
    while True:
        
        pawn = textinput(f"Ruch gracza {gracz}", "Podaj pionka, którego ma postawić twój przeciwnik: ")          #Drobna zmiana, żeby [Menu] przerywało rozgrywkę
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
def place_pawn(board, pawn, gracz):
    while True:
        position = textinput(f"Ruch gracza {gracz}", f"Podaj pole (|00| - |33|) na które chcesz postawić pionka {pawn}: ")
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
    tracer(0, 1)
    penup()
    goto(x, y)
    pendown()


def draw_square(side, colour, x, y):
    tracer(0, 1)
    pencolor(colour)
    side = int(round(side))
    if side % 2 == 1:
        side += 1
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
    pencolor("black")


def draw_circle(side, colour, x, y):
    pencolor(colour)
    tracer(0, 1)
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
    pencolor("black")


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


def draw_pawn(x, y, side, board):  # side to dlugosc boku/srednicy pionka, x y to jego miejsce na boardzie
    tracer(0, 1)
    length = side * 5 / 4 / 2   # length to odleglosc srodka pionka od kratki boarda. Pierwsze dwie liczby okreslaja stosunek kratki boarda do wielkosci pionka.
    colour = board.board[x][y].attributes[0]
    height = board.board[x][y].attributes[1]
    shape1 = board.board[x][y].attributes[2]
    dot1 = board.board[x][y].attributes[3]
    x = ret_x(x, length)
    y = ret_x(y, length) + 290
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


def write_row(position1, number, length):
    tracer(0, 1)
    x = position1[0] - 20
    y = position1[1]
    y += length
    move(x, y)
    write(number)


def write_col(position1, number, length):
    tracer(0, 1)
    x = position1[0]
    y = position1[1] - 20
    x += length
    move(x, y)
    write(number)


def draw_board(x, y, pawn_side):  # x, y to wspolrzedne srodka boarda
    width(2)
    tracer(0, 1)
    hideturtle()
    length = pawn_side * 5 / 4 / 2
    board_side = pawn_side * 5

    # poziome kreski i podpisy
    move(x,y)
    forward(board_side/2)
    backward(board_side)
    write_row(position(), 2, length)

    move(0, y + board_side / 4)
    forward(board_side / 2)
    backward(board_side)
    write_row(position(), 3, length)

    move(0, y - board_side / 4)
    forward(board_side / 2)
    backward(board_side)
    write_row(position(), 1, length)

    move(position()[0] + 20, y - board_side / 2)
    write_row(position(), 0, length)

    # pionowe kreski i podpisy
    move(x, y)
    setheading(90)

    forward(board_side / 2)
    backward(board_side)
    write_col(position(), 2, length)

    move(x + board_side / 4, y)
    forward(board_side / 2)
    backward(board_side)
    write_col(position(), 3, length)

    move(x - board_side / 4, y)
    forward(board_side / 2)
    backward(board_side)
    write_col(position(), 1, length)

    move(x - board_side/2, position()[1] + 20)
    write_col(position(), 0, length)
    width(1)

    update()


def pawn_list(x, lista_pionków, side):
    tracer(0, 1)
    y = round(len(lista_pionków) * side * 5 / 4 / 2) # dlugosc naszej listy / 2
    oryg_side = side
    move(x, 0)

    #wymazujemy starą listę pionków
    pencolor("white")
    fillcolor("white")
    begin_fill()
    setheading(0)
    fd((oryg_side + 100) / 2)
    setheading(90)
    fd(500)
    setheading(180)
    fd(oryg_side + 100)
    setheading(270)
    fd(1000)
    setheading(0)
    fd(oryg_side + 100)
    setheading(90)
    fd(500)
    end_fill()
    pencolor("black")

    for pionek in lista_pionków:  # Wyświetla dostępne pionki wraz z atrybutami
        side = oryg_side
        move(x, y)
        colour = pionek.attributes[0]
        height = pionek.attributes[1]
        shape1 = pionek.attributes[2]
        dot1 = pionek.attributes[3]
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

        write_row((x-40, position()[1]), pionek.id, 0)
        y -= round(oryg_side * 5 / 4)
        update()
