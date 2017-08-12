import copy
import math
import time


class Polynomial:
    def __init__(self, c):
        self.coefs = c

    def __repr__(self):
        prnt_str = ""
        for deg, coef in enumerate(self.coefs):
            if coef > 0 and deg != 0:
                prnt_str += " + " + str(coef) + "*x^" + str(deg)
            elif coef > 0 and deg == 0:
                prnt_str += str(coef) + "*x^" + str(deg)
            elif coef < 0:
                prnt_str += " - " + str(-coef) + "*x^" + str(deg)
        if prnt_str != "" and (prnt_str[1] == '+' or prnt_str[1] == '1'):
            prnt_str = prnt_str[3:]
        return prnt_str

    def __add__(self, other):
        poly = copy.deepcopy(self)
        for i in range(len(other.coefs)):
            if i < len(self.coefs):
                poly.coefs[i] += other.coefs[i]
            else:
                poly.coefs.append(other.coefs[i])
        return poly

    def __sub__(self, other):
        poly = Polynomial([])
        for i in range(len(other.coefs)):
            if i < len(self.coefs):
                poly.coefs.append(self.coefs[i] - other.coefs[i])
            else:
                poly.coefs.append(0-other.coefs[i])
        return poly

    def __mul__(self, other):
        poly = Polynomial([0] * (len(self.coefs) + len(other.coefs) - 1))  # Length is sum of highest degree + 1
        for deg1, coef1 in enumerate(self.coefs):
            for deg2, coef2 in enumerate(other.coefs):
                # Multiplies coefficients and places them in the index related to
                # the sum of the degrees of x
                poly.coefs[deg1 + deg2] += coef1 * coef2
        return poly

    def __len__(self):
        return len(self.coefs)

    def degree(self):
        poly = self.coefs[:]
        while poly[-1] == 0:
            poly.pop()
        return len(poly) - 1


class Board:
    def __init__(self, h, w, bad_sqrs):
        self.height = h
        self.width = w
        self.board = {}
        for i in range(h):
            self.board[i] = {}
            for j in range(w):
                if (i, j) in bad_sqrs:
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = 1

    def __repr__(self):
        prnt_str = ""
        for row in self.board.values():
            for sqr in row.values():
                prnt_str += str(sqr) + " "
            prnt_str += "\n"
        return prnt_str

    def is_single_cell(self):
        rows = []
        for row in self.board.values():
            rows.append(int("".join(str(x) for x in row.values()), 2))
        cells = []
        for n in rows:
            cells.append(NumberOfSetBits(n))
        if cells.count(1) == 1 and set(cells) == {0, 1}:
            return True
        return False

    def is_empty(self):
        rows = set(tuple(i.values()) for i in list(self.board.values()))
        if len(rows) == 1:
            if int("".join(str(x) for x in rows.pop()), 2)== 0:
                return True
        return False

    def build_B_i_and_B_e(self):
        B_i = Board(self.height, self.width, {})
        B_i.board = copy.deepcopy(self.board)
        B_e = Board(self.height, self.width, {})
        B_e.board = copy.deepcopy(self.board)
        for i in range(len(B_i.board)):
            for j in range(len(B_i.board)):
                if B_i.board[i][j]:
                    for row in range(len(B_i.board)):
                        if i == row:
                            for val in B_i.board[row]:
                                B_i.board[row][val] = 0
                        B_i.board[row][j] = 0
                    B_e.board[i][j] = 0
                    return B_i, B_e

    def find_rook_polynomial(self):
        # R_of_B = Polynomial([])
        if self.is_empty():
            return Polynomial([1])
        if self.is_single_cell():
            return Polynomial([1, 1])
        else:
            B_i, B_e = self.build_B_i_and_B_e()
            be = B_e.find_rook_polynomial()
            bix = (B_i.find_rook_polynomial() * Polynomial([0, 1]))
            R_of_B = be + bix  # B_e.find_rook_polynomial() + (B_i.find_rook_polynomial() * Polynomial([0, 1]))
        return R_of_B


def binomial(n, k):
    if n > 0:
        return int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))
    elif n == 0:
        return 0
    elif n < 0:
        return None


def NumberOfSetBits(i):
    i -= (i >> 1) & 0x55555555
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24


# b = Board(3, 3, {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)})
bad = {(i,i) for i in range(5)}
bad.add((1,4))
b = Board(7, 7, {})
print(b)
print()
start = time.time()
print(b.find_rook_polynomial())
print("\n", time.time() - start)
# p = Polynomial([1,1,1])
# q = Polynomial([1,1])
# print(p)
# print(q)
# print(q+p)


