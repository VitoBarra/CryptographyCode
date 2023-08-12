import math

def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def Generate_perfect_squares(start, end):
    perfect_squares = []
    for num in range(start, end + 1):
        if is_perfect_square(num):
            perfect_squares.append(num)
    return perfect_squares