class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def get_element_at(self, position):
        if not self.head:
            return None

        temp = self.head
        for _ in range(position):
            temp = temp.next
            if temp == self.head:
                return None  # La posición está más allá del final de la lista circular

        return temp.data

# Crear una lista circular simple
clist = CircularLinkedList()

# Agregar elementos a la lista
clist.append('Casio')
clist.append('Tissot')
clist.append('Realme')
clist.append('Binden')
clist.append('Samsung')
clist.append('Fossol')
clist.append('Rolex')
clist.append('Timex')

# Mostrar la lista circular
print("Lista Circular:")
clist.display()
elemet = int(input("coloca tu numero de consulta"))
element = clist.get_element_at(elemet)
if element is not None:

    print(clist.get_element_at(elemet))
else:
    print("pendeja")