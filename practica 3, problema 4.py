import math
b = float(input("inserta el tamaño del primer lado "))
c = float(input("inserta el tamaño del segundo lado "))
alfa = float(input("cual es el angulo que forma en grados sexagesimales "))
alfa = alfa * 3.1416 / 180
cos=math.cos(alfa)
a = b*b + c*c - 2*b*c * cos
a = pow(a,1/2)
print("el tercer lado mide ",a)
