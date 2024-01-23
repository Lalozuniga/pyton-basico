class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def traverse(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()

# Ejemplo de uso
clist = CircularDoublyLinkedList()
clist.append('pantalon')
clist.append('sueter')
clist.append('camisa')
clist.append('sombrero')
clist.append('zapatos')
clist.append('chaqueta')
clist.append('gorra')
clist.traverse()
