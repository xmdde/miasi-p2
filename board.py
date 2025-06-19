class Piece:
    def __init__(self, color, col, row):
        self.color = color
        self.col = col  # e.g. 'e'
        self.row = row  # e.g. 2

    def symbol(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def position_indices(self):
        x = ord(self.col.lower()) - ord('a')
        y = self.row - 1
        return x, y

"""
class Pawn(Piece):
    def symbol(self):
        return 'P' if self.color == 'White' else 'p'

class Rook(Piece):
    def symbol(self):
        return 'R' if self.color == 'White' else 'r'

class Knight(Piece):
    def symbol(self):
        return 'N' if self.color == 'White' else 'n'

class Bishop(Piece):
    def symbol(self):
        return 'B' if self.color == 'White' else 'b'

class Queen(Piece):
    def symbol(self):
        return 'Q' if self.color == 'White' else 'q'

class King(Piece):
    def symbol(self):
        return 'K' if self.color == 'White' else 'k'
"""

class Pawn(Piece):
    def symbol(self):
        return '♙' if self.color == 'White' else '♟'

class Rook(Piece):
    def symbol(self):
        return '♖' if self.color == 'White' else '♜'

class Knight(Piece):
    def symbol(self):
        return '♘' if self.color == 'White' else '♞'

class Bishop(Piece):
    def symbol(self):
        return '♗' if self.color == 'White' else '♝'

class Queen(Piece):
    def symbol(self):
        return '♕' if self.color == 'White' else '♛'

class King(Piece):
    def symbol(self):
        return '♔' if self.color == 'White' else '♚'

class Board:
    def __init__(self, size):
        self.size = size
        self.pieces = list()

    def add_piece(self, piece):
        self.pieces.append(piece)

    def setup_board(self):
        self.add_pieces()

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


    def add_pieces(self):
        for i in range(8):
            col = chr(ord('a') + i)
            self.add_piece(Pawn("White", col, 2))
            self.add_piece(Pawn("Black", col, 7))

        self.add_piece(Rook("White", 'a', 1))
        self.add_piece(Rook("White", 'h', 1))
        self.add_piece(Rook("Black", 'a', 8))
        self.add_piece(Rook("Black", 'h', 8))

        self.add_piece(Knight("White", 'b', 1))
        self.add_piece(Knight("White", 'g', 1))
        self.add_piece(Knight("Black", 'b', 8))
        self.add_piece(Knight("Black", 'g', 8))

        self.add_piece(Bishop("White", 'c', 1))
        self.add_piece(Bishop("White", 'f', 1))
        self.add_piece(Bishop("Black", 'c', 8))
        self.add_piece(Bishop("Black", 'f', 8))

        self.add_piece(Queen("White", 'd', 1))
        self.add_piece(Queen("Black", 'd', 8))

        self.add_piece(King("White", 'e', 1))
        self.add_piece(King("Black", 'e', 8))

def demo():
    board = Board(8)
    board.setup_board()
    board.print_board()

if __name__ == "__main__":
    demo()

