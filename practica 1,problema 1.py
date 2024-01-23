def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
contador = 0
numero_actual = 2

while contador < 10:
    if es_primo(numero_actual):
        print(f"{numero_actual}   -   {numero_actual**3}")
        contador += 1
    numero_actual += 1
