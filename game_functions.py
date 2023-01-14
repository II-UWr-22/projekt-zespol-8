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
                return None
            else:
                print("Pozycja zajęta")
        except:
            print("Podaj poprawną pozycję")


def check_for_win():
    #TODO
    pass