class Board:
    def __init__(self, h, w, bad_sqrs):
        self.height = h
        self.width = w
        self.board = {}
        for i in range(h):
            self.board[i] = {}
            for j in range(w):
                if (i, j) in bad_sqrs or (j, i) in bad_sqrs:
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = 1
        return

    def __repr__(self):
        prnt_str = ""
        for row in self.board.values():
            for sqr in row.values():
                prnt_str += str(sqr) + " "
            prnt_str += "\n"
        return prnt_str

    def find_rook_polynomial(self):
        rook_polynomial = []
        return rook_polynomial


board = Board(2, 2, {})
print(board)
print()
print(board.find_rook_polynomial())


_pc = []
for i in range(256):
    c = 0
    while i:
        # clear last set bit
        i &= i-1
        c += 1
    _pc.append(c)

def popcount(i):
    "Return number of bits set."
    result = 0
    while i:
        result += _pc[i & 0xff]
        i >>= 8
    return result

def perm(a):
    "Return permanent of 0-1 matrix.  Each row is an int."
    result = 0
    n = len(a)
    for s in range(1 << n):
        prod = 1
        for row in a:
            prod *= popcount(row & s)
        if popcount(s) & 1:
            result -= prod
        else:
            result += prod
    if n & 1:
        result = -result
    return result

def matrix2ints(a):
    return [int("".join(map(str, row)), 2)
            for row in a]

def matrix_perm(a):
    "Return permanent of 0-1 matrix."
    return perm(matrix2ints(a))

print(matrix_perm([[1,1,0,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))