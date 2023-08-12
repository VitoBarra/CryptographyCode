import math
import MyMath.ModAlgebraUtils as md


class ElliptCurve:
    def __init__(self,a,b,p):
        self.a =a
        self.b =b
        self.p =p
        self.xpoint = self.GeneratePoint_list(p,self.XPart)
        self.ypoint = self.GeneratePoint_list(p,self.YPart)

    def XPart(self,x):
        return x**3 + self.a*x + self.b
    def YPart(self,y):
        return y**2

    def GeneratePoint_list(self,p,f):
        point =[]
        for i in md.Generate_Z_set(p):
            point.append(f(i) % p)
        return point

    
    def Create_curve_point_matrix(self, func):
        matrix = []
        for i in range(len(self.xpoint)):
            row = []
            for j in range(len(self.ypoint)):
                value = func(self.xpoint[j], self.ypoint[i])
                row.append(value)
            matrix.append(row)
        return matrix
