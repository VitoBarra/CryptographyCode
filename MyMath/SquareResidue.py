import MyMath.PerfectSquare as ps
from tabulate import tabulate


def calculate_quadratic_residuals(squares,prime):
    residuals = []
    res =[]
    for sq in squares:
        v = sq % prime

        if(v not in residuals):
            res.append((sq,v))
            residuals.append(v)
    return res



def Get_quadratic_residuals(prime):
    perfect_squares = ps.Generate_perfect_squares(0, prime*100)
    return calculate_quadratic_residuals(perfect_squares,prime)

def print_quadratic(prime):
    quadratic_residuals = Get_quadratic_residuals(prime)
    print("numero primo: ",prime)
    print ("si sta gli scarti quadratici con la formula y^2=x mod",prime, "come da definizione\n")
    table = tabulate(quadratic_residuals, headers=["perfect square","quadratic residue"], tablefmt="grid")
    print(table)
    print ("\nil numero di scarti quadratici trovati è:", len(quadratic_residuals), "i quadrati aspettati sono" ,(prime-1)/2+1)



