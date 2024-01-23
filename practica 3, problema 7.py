print("Determine la distancia entre dos puntos en el espacio")

print("Dame los valores del primer punto")
x1 = int(input("x ="))
y1 = int(input("y ="))
z1 = int(input("z ="))

print("Dame los valores del segundo punto")
x2 = int(input("x ="))
y2 = int(input("y ="))
z2 = int(input("z ="))

x= (x2-x1)**2
y= (y2-y1)**2
z= (z2-z1)**2

a=x+y+z
d = pow(a,1/2)
print("la distacia es ", d)