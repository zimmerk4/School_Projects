import copy
import math


def binomial(n, k):
    if n > 0:
        return int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))
    elif n == 0:
        return 0
    elif n < 0:
        return None

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
        poly = Polynomial([])
        for i in range(len(other.coefs)):
            if i < len(self.coefs):
                poly.coefs.append(self.coefs[i] + other.coefs[i])
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

    def is_square(self):
        for row in self.board:
            for val in self.board[row]:
                if self.board[row][val] == 0:
                    return False
        return True

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
        R_of_B = Polynomial([])
        if len(self.board) == 0:
            return Polynomial([1])
        if self.is_square():
            for k in range(self.height + 1):
                R_of_B.coefs.append(binomial(self.height, k)*binomial(self.height, k)*math.factorial(k))
            return R_of_B
        B_i, B_e = self.build_B_i_and_B_e()
        R_of_B = B_i.find_rook_polynomial() + B_e.find_rook_polynomial()
        return R_of_B


board = Board(2, 2, {(0,1)})
print(board)
# print()
# b_i, b_e = board.build_B_i_and_B_e()
# print(b_e)
# print()
# print(b_i)
print()
print(board.find_rook_polynomial())
