import math
import Prime_lib
from tabulate import tabulate

def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def find_perfect_squares(start, end):
    perfect_squares = []
    for num in range(start, end + 1):
        if is_perfect_square(num):
            perfect_squares.append(num)
    return perfect_squares

def calculate_quadratic_residuals(squares,prime):
    
    residuals = []
    res =[]
    for sq in squares:
        v = sq % prime

        if(v not in residuals):
            res.append((sq,v))
            residuals.append(v)
    return res







def print_quadratic(prime):
    perfect_squares = find_perfect_squares(0, prime*100)
    quadratic_residuals = calculate_quadratic_residuals(perfect_squares,prime)
    print("numero primo: ",prime)
    print ("si sta gli scarti quadratici con la formula y^2=x mod",prime, "come da definizione\n")
    table = tabulate(quadratic_residuals, headers=["perfect square","quadratic residue"], tablefmt="grid")
    print(table)
    print ("\nil numero di scarti quadratici trovati è:", len(quadratic_residuals), "i quadrati aspettati sono" ,(prime-1)/2+1)



#print_quadratic(Prime_lib.generate_random_prime(50,100))
print_quadratic(7)

