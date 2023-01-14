#Wybiera pionka po id, usuwa go z dostępnych i zwraca id
def choose_pawn(board):
    while True:
        
        pawn = input("Podaj pionka którego ma postawić twój przeciwnik: ")          #Drobna zmiana, żeby [Menu] przerywało rozgrywkę
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


#Kładzie pionka na wybranym polu
def place_pawn(board,pawn):
    while True:
        position = input(f"Podaj pole na które chcesz postawić pionka {pawn}: ")
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