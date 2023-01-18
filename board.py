from game_functions import place_pawn, choose_pawn
class Piece:
    # defines Piece properties (please modify satisfy to board drawing)
    # each piece has exactly 4 attributes, and each attribute
    # can be one out of the 2 options
    possible_attributes = [
        ("light", "dark"),
        ("short", "tall"),
        ("circle", "square"),
        ("has dot", "no dot"),
    ]
    # id: int from 0 to 15 which is a unique identifier based on attributes
    id: int
    # attributes: 4-len tuple of strings, please refer to piece_attributes
    attributes: tuple[str]

    def __init__(self, id=None, attrs=None) -> None:
        if id is None and attrs is None:
            raise TypeError("Piece cannot be None")

        if attrs is None:
            self.id = id
            self.attributes = Piece.id_to_attributes(self.id)

        elif id is None:
            self.id = Piece.attributes_to_id(attrs)
            self.attributes = attrs
        else:
            raise Exception("Please enter either id or attrs!")

    # generate attributes based on id (static function, aka you don't run it on an instance)
    def id_to_attributes(id: int):
        # parse to 4-len binary string
        if id not in range(16):
            raise ValueError("invalid id, expected: {}, found {}".format("0 - 15", id))

        id_str = "{:b}".format(id).zfill(4)
        id_map = map(int, id_str)
        return [Piece.possible_attributes[i][option] for i, option in enumerate(id_map)]

    # generate id based on attributes (static function, aka you don't run it on an instance)
    def attributes_to_id(attrs):
        is_valid = all(attr in options for attr, options in zip(attrs, Piece.possible_attributes))
        if not is_valid:
            raise ValueError("Invalid attributes,\nexpected: {},\nfound: {}".format(Piece.possible_attributes, attrs))

        which_options = [options.position(attr) for attr, options in zip(attrs, Piece.possible_attributes)]
        id_str = "".join(str(i) for i in which_options)
        return str(id_str)

    # TODO: prettier str representation
    def __str__(self) -> str:
        return f"{str(self.id)}     {' | '.join(self.attributes)}"

    def __repr__(self) -> str:
        return f"{__name__}({self.id=}, {self.attributes=})"


class Board:
    board: tuple[tuple[Piece | None]]
    pieces_position: tuple[tuple[int, int] | None]

    def __init__(self) -> None:
        self.board = [[None] * 4 for _ in range(4)]
        self.pieces_position = [None] * 16
        #(Tymczasowo) trzyma id dostępnych pionków
        self.available_pieces = [i for i in range(16)]

    def __str__(self) -> str:
        line = "+" + "-" * 25 + "+\n"
        inner = ""
        for row_index,row in enumerate(self.board):
            inner += "|" + "  \t".join(f" {str(piece.id):>2} " if piece else f"|{row_index}{piece_index}|" for piece_index,piece in enumerate(row)) + "|\n"

        return line + inner + line

    def set_piece(self, x: int, y: int, piece_id: int):
        if self.pieces_position[piece_id]:
            raise ValueError("Piece has been already placed")
        self.board[x][y] = Piece(id=piece_id)
        self.pieces_position[piece_id] = (x, y)

