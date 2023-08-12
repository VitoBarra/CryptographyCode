import MyMath.ElliptCurve as ec
import MyMath.SquareResidue as sr
from tabulate import tabulate

p =13
Ellipsis = ec.ElliptCurve(1,0,p)

#sr.print_quadratic(Prime_lib.generate_random_prime(50,100))
#sr.print_quadratic(7)

convert_to_binary = lambda x: "X" if x else ""
result_matrix =Ellipsis.Create_curve_point_matrix(lambda x, y: convert_to_binary(x == y))
table = tabulate(result_matrix, headers=Ellipsis.xpoint,showindex=Ellipsis.ypoint, tablefmt="grid")

print(table)
print(sr.Get_quadratic_residuals(p))
# i numeri che non sono scarti quadratici non compaiono proprio trai possibili valori di y**2 mod p
#for row in result_matrix:
 #   print(row)
