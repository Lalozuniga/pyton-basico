from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")
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
            return ""
        result = []
        temp = self.head
        while True:
            result.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(map(str, result))

clist = CircularLinkedList()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]
        if data:
            clist.append(data)
    return render_template("index.html", circular_list=clist.display())

if __name__ == "__main__":
    app.run(debug=True)
