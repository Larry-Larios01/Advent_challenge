class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None

# Clase Lista Enlazada
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node

    def find_next_node(self, current_node):
        """Devuelve el siguiente nodo dado un nodo actual."""
        if current_node.next:
            return current_node.next  
        else:
            return None 
        


ll = LinkedList()


splitted = [1,2,3,4,5]

for split in splitted:
    ll.insert_at_end(split)


current = ll.head
ok_reports = 0
while current: 
    next_node = ll.find_next_node(current)
    if next_node:
        result = abs(current.data-next_node.data)
        #print(result)
        if result != 1 and result !=  2:
            break
        current = current.next
    if not next_node:
        print("listo")
        ok_reports += 1
        break


print(ok_reports)




