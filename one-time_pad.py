import random


CHARKEY = {' ': "00", 'A': "01", 'B': "02", 'C': "03", 'D': "04", 'E': "05",
           'F': "06", 'G': "07", 'H': "08", 'I': "09", 'J': "10", 'K': "11",
           'L': "12", 'M': "13", 'N': "14", 'O': "15", 'P': "16", 'Q': "17",
           'R': "18", 'S': "19", 'T': "20", 'U': "21", 'V': "22", 'W': "23",
           'X': "24", 'Y': "25", 'Z': "26"}
INV_CHARKEY = {val: key for key, val in CHARKEY.items()} #inverse of CHARKEY

def fib_add(n, m):
    """
    :param n: zero padded fixed length string representing integer
    :param m: zero padded fixed length string representing integer
    :return: zero padded fixed length string of integer where each digit is the
             sum of the analogous digits in n and m modulo 10
    """
    n_plus_m = ""
    # i is position of digit with rightmost digit being 0
    for i in range(len(n) - 1, -1, -1):
        n_plus_m += str((int(n[i]) + int(m[i])) % 10)
    return n_plus_m[::-1]  # reverses string


def fib_sub(n, m):
    """
    :param n: zero padded fixed length string representing integer
    :param m: zero padded fixed length string representing integer
    :return: zero padded fixed length string of integer where each digit is the
             difference of the analogous digits in n and m modulo 10
    """
    n_minus_m = ""
    # i is position of digit with rightmost digit being 0
    for i in range(0, len(n)):
        n_minus_m += str((int(n[i]) - int(m[i])) % 10)
    return n_minus_m


def generate_pad(n, f1):
    """
    :param n: number of random integers between 00 and 99 to generate
    :param f1: string of file name
    :return: none
    """
    with open(f1, 'w') as file:
        for i in range(n):  # Write n space delimited random integers to f1
            file.write("{0:02d} ".format(random.randint(0,99)))
    return


def encrypt(s, f1, f2):
    n = len(s)
    generate_pad(n, f1)
    with open(f1, 'r') as file1:
        key_nums = file1.readline().split()  # tuple of strings of nums in key
        with open(f2, 'w') as file2:
            for i in range(len(s)):
                # write space separated sum of key number and char value into f2
                file2.write(fib_add(key_nums[i], CHARKEY[s[i]]) + ' ')
    return


def dencrypt(f1, f2):
    message = ""
    with open(f1, 'r') as file1:
        key_nums = file1.readline().split()  # tuple of strings of nums in key
        with open(f2, 'r') as file2:
            # tuple of strings of nums in encrypted message
            mssg_nums = file2.readline().split()
        for i in range(len(mssg_nums)):
            # write space separated sum of key number and char value into f2
            message += INV_CHARKEY[fib_sub(mssg_nums[i], key_nums[i])]
    print(message)
    return message

# Test "HELLO"
encrypt("HELLO", "f1", "f2")
assert dencrypt("f1", "f2") == "HELLO"

# Test "FART"
encrypt("FART", "f1", "f2")
assert dencrypt("f1", "f2") == "FART"

# Test "IT WORKS IT REALLY WORKS"
encrypt("IT WORKS IT REALLY WORKS", "f1", "f2")
assert dencrypt("f1", "f2") == "IT WORKS IT REALLY WORKS"

# Test "TOO BAD THERES NO PUNCTUATION HERE WE JUST GET REALLY LARGE RUN ON
# SENTENCES THAT ARE VERY CONFUSING TO READ BUT I SUPPOSE THE PROJECT IS EASILY
# EXTENDABLE TO PUNCTUATION DIGITS AND LOWERCASE LETTERS AS WELL"
encrypt("TOO BAD THERES NO PUNCTUATION HERE WE JUST GET REALLY LARGE RUN ON SEN\
TENCES THAT ARE VERY CONFUSING TO READ BUT I SUPPOSE THE PROJECT IS EASILY EXTE\
NDABLE TO PUNCTUATION DIGITS AND LOWERCASE LETTERS AS WELL", "f1", "f2")
assert dencrypt("f1", "f2") == "TOO BAD THERES NO PUNCTUATION HERE WE JUST GET \
REALLY LARGE RUN ON SENTENCES THAT ARE VERY CONFUSING TO READ BUT I SUPPOSE THE\
 PROJECT IS EASILY EXTENDABLE TO PUNCTUATION DIGITS AND LOWERCASE LETTERS AS WEL\
L"
