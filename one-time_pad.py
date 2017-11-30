import random


def generate_pad(n, f1):
    """
    Takes integer, n,  and file location string, f1,  and generates n random
    integers between 00 and 99
    """
    with open(f1,'w' ) as file:
        for i in range(n):
            file.write("{0:02d} ".format(random.randint(0,99)))
    return

def encrypt(s, f1, f2):
    n = len(s)
    generate_pad(n, f1)
    with open(f1, 'r') as file1:
        nums = [int(num) for num in file1.readline().split()]


    return

def decrypt(f1, f2):
    return

#generate_pad(10,"f1")
encrypt("Hello", "f1", 5)