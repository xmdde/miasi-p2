
class Piece:
    def __init__(self, color, col, row):
        self.color = color
        self.col = col
        self.row = row

    def symbol(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def position_indices(self):
        x = ord(self.col.lower()) - ord('a')
        y = self.row - 1
        return x, y


class Queen(Piece):
    def symbol(self):
        return 'Q' if self.color == 'White' else 'q'

class Bishop(Piece):
    def symbol(self):
        return 'B' if self.color == 'White' else 'b'

class Rook(Piece):
    def symbol(self):
        return 'R' if self.color == 'White' else 'r'

class Pawn(Piece):
    def symbol(self):
        return 'P' if self.color == 'White' else 'p'

class Knight(Piece):
    def symbol(self):
        return 'N' if self.color == 'White' else 'n'

class King(Piece):
    def symbol(self):
        return 'K' if self.color == 'White' else 'k'


class Board:
    def __init__(self, size):
        self.size = size
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def print_board(self):
        board = [["." for _ in range(self.size)] for _ in range(self.size)]
        for piece in self.pieces:
            x, y = piece.position_indices()
            if 0 <= x < self.size and 0 <= y < self.size:
                board[y][x] = piece.symbol()

        col_labels = [chr(ord('a') + i) for i in range(self.size)]
        top_row = "    " + "   ".join(col_labels)
        divider = "  +" + "---+" * self.size

        print(top_row)
        for row_idx in reversed(range(self.size)):
            print(divider)
            row_str = f"{row_idx + 1} |"
            for col_idx in range(self.size):
                row_str += f" {board[row_idx][col_idx]} |"
            print(row_str + f" {row_idx + 1}")
        print(divider)
        print(top_row)

class GameBoard(Board):
    def __init__(self):
        super().__init__(8)
        self.move_history = []
        self.setup()

    def setup(self):
        self.add_piece(Pawn("Black", 'c', 7))
        self.add_piece(Pawn("Black", 'b', 7))
        self.add_piece(Pawn("White", 'd', 2))
        self.add_piece(Rook("White", 'a', 1))
        self.add_piece(Pawn("White", 'g', 2))
        self.add_piece(Knight("White", 'g', 1))
        self.add_piece(Pawn("White", 'e', 2))
        self.add_piece(Pawn("White", 'b', 2))
        self.add_piece(Rook("Black", 'h', 8))
        self.add_piece(Queen("White", 'd', 1))
        self.add_piece(Pawn("Black", 'd', 7))
        self.add_piece(Bishop("Black", 'f', 8))
        self.add_piece(Pawn("Black", 'a', 7))
        self.add_piece(Knight("Black", 'b', 8))
        self.add_piece(Pawn("White", 'f', 2))
        self.add_piece(Pawn("Black", 'h', 7))
        self.add_piece(Knight("White", 'b', 1))
        self.add_piece(King("Black", 'e', 8))
        self.add_piece(Pawn("White", 'a', 2))
        self.add_piece(Pawn("Black", 'g', 7))
        self.add_piece(Bishop("White", 'f', 1))
        self.add_piece(Bishop("White", 'c', 1))
        self.add_piece(Pawn("White", 'h', 2))
        self.add_piece(Knight("Black", 'g', 8))
        self.add_piece(Pawn("Black", 'e', 7))
        self.add_piece(Queen("Black", 'd', 8))
        self.add_piece(King("White", 'e', 1))
        self.add_piece(Rook("Black", 'a', 8))
        self.add_piece(Pawn("Black", 'f', 7))
        self.add_piece(Rook("White", 'h', 1))
        self.add_piece(Bishop("Black", 'c', 8))
        self.add_piece(Pawn("White", 'c', 2))

if __name__ == "__main__":
    board = GameBoard()
    board.setup()
    board.print_board()
