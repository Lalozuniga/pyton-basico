#cantidad de litros en galones
l= 3.78541
#precio de la gasolina
print("Cual es el precio de la gasolina por galones")
p = float(input())
#litros suministrados al cliente
print("cuantos  galones de gasolina se le vendieron al cliente ")
g = float(input())

lf = g * l
print(g," galones es igual a ", lf, " litros")
lf = lf * p
print("por ",g , " galones de gasolina debes cobrarle al cliente ",lf)