
print("ingresa las cordenadas del punto A")
AX = int(input("ingresa la cordenada x"))
AY = int(input("ingresa la cordenada Y"))
print("ingresa las cordenadas del punto B")
BX = int(input("ingresa la cordenada x"))
BY = int(input("ingresa la cordenada Y"))
A1 = AX - BX
X = A1 * A1
B1 = AY - BY
Y = B1 *B1
C = X+Y

a = pow( C, 1/2)

print("la distancia es ", a)