class node():
    def __init__(self, data):
        self.data = data
        self.next = None 

class linkedlist():
    def __init__(self):
        self.head = None

    def show_list(self):
        lst = self.head
        print(lst.data)
        while lst.next != None :            
            lst = lst.next
            print(lst.data)


a = node(1)
b = node(2)
c = node(3)
d = node(4)
a.next = b
b.next = c
c.next = d

ll = linkedlist()
ll.head = a
ll.show_list()