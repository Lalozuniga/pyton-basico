class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_posicion(self, posicion):
        if posicion < 0:
            print("La posición debe ser mayor o igual a 0.")
            return
        actual = self.cabeza
        indice = 0
        while actual:
            if indice == posicion:
                print(f"Valor en la posición {posicion}: {actual.valor}")
                return
            actual = actual.siguiente
            indice += 1
        print(f"No se encontró un elemento en la posición {posicion}.")


# Crear una lista enlazada simple y agregar algunos valores
ropa_mexicana = ListaEnlazadaSimple()
ropa_mexicana.append('EDHER GZN')
ropa_mexicana.append('NO NAME STUDIO')
ropa_mexicana.append('CIENTO CINCUENTA Y SIETE')
ropa_mexicana.append('DAVE')
ropa_mexicana.append('EDDIE CORPS')
ropa_mexicana.append('ELIZABETH SILVA')
ropa_mexicana.append('IVAN AVALOS')

# Imprimir la lista
ropa_mexicana.imprimir()
ropa_mexicana.imprimir_posicion(0)