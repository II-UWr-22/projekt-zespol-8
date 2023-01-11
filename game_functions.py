#Wybiera pionka po id, usuwa go z dostępnych i zwraca id
def choose_pawn(board):
    while True:
        try:
            pawn = int(input("Podaj pionka którego ma postawić twój przeciwnik: "))
        except:
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
        try:
            x,y = int(position[0]),int(position[1])
            board.set_piece(x, y, pawn)
            break
        except:
            print("Podaj poprawną pozycję")