n = int(input("de cuantos alumnos quieres sacar el promedio?"))
p = 0
i= 1
while i<=n :
    A = input("ingresa el nombre del alumno ")
    print("ingresa las calificaciones de ", A)
    n1 = int(input("calificacion 1 del alumno "))
    n2 = int(input("calificacion 2 del alumno "))
    n3 = int(input("calificacion 3 del alumno "))
    promedio = (n1 + n2 + n3) / 3
    print("el promedio de ", A, "es", promedio)
    i = i + 1
    p = p + promedio
f = p / n
print("el promedio de todos los alumnos es ", f)
