class Board:
    def __init__(self, h, w, bad_sqrs):
        self.height = h
        self.width = w
        self.board = []
        for i in range(h):
            self.board.append([])
            for j in range(w):
                if (i, j) in bad_sqrs:
                    self.board[i].append(0)
                else:
                    self.board[i].append(1)
        return

    def __repr__(self):
        prnt_str = ""
        for row in self.board:
            for sqr in row:
                prnt_str += str(sqr) + " "
            prnt_str += "\n"
        return prnt_str





board = Board(4, 4, {(0, 2), (2, 0)})
print(board)
