n = input("cual es el nombre de tu equipo")
A = int(input("cuantos partidos gano tu equipo"))
A1 = A*3
print("tu equipo tiene ", A1 ,"puntos")
B = int(input("cuantos partidos perdio"))
print("tu equipo tiene ", A1 ,"puntos")
C = int(input("cuantos partidos empato"))
A2 = A1 + C
print("tu equipo tiene ", A2 ,"puntos")
print("el equipo", n)
print("gano",A, " partidos y obtuvo ", A1 )
print("tu equipo tuvo ", B, " derrotas y no sumo punto")
print("tu equipo empato ", C, " partido y sumo ",C)
A3 = A+B+C
print("el equipo jugo ", A3, "partidos")