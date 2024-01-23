
n = int(input("Ingrese el valor de n: "))

# Definimos los valores iniciales de la progresión
a1 = 10   # Primer término de la progresión
d = 5     # Diferencia común entre los términos de la progresión

# Calculamos el término final de la progresión
Tn = a1 + (n-1)*d

# Calculamos la suma de la progresión aritmética
suma = ((a1 + Tn)*n) / 2

# Imprimimos el resultado
print("La suma de los términos de la progresión aritmética es:", suma)