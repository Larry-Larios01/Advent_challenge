import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

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




# URL de la página
url = "https://adventofcode.com/2024/day/2/input"

# Realizar solicitud HTTP

session = os.getenv("SESSION")
cookies = {'session': session}

#response = requests.get(url, cookies=cookies)


response = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
#print(response.text)

def dampener_checker(link: LinkedList):
    return True



text_strip = response.strip().split("\n")
print(text_strip)

ok_reports = 0
for item in text_strip:
    splitted = item.split()
    print(splitted)
    ll = LinkedList()

    for split in splitted:
        ll.insert_at_end(split)

   

    current = ll.head
    is_safe = True
    incre_decre = ""
    problem_dampener = 0
    while current: 
        next_node = ll.find_next_node(current)

        print("teh next node", next_node)
        if next_node:
            result = abs(current.data-next_node.data)
            if current.data> next_node.data:
                if incre_decre == "i":
                    dampener = dampener_checker(ll)
            
                    is_safe = False
                    break
                    
                elif incre_decre is not "i":
                    incre_decre = "d"

            if current.data < next_node.data:
                if incre_decre == "d":

                    is_safe = False
                    break
                    
                elif incre_decre is not "d":
                    incre_decre = "i"
            if result < 1 or result>3:
                    is_safe = False
                    break
                
            current = current.next
            print("the current", current.data)
        if not next_node:
            current =  current.next
        

    if is_safe:
        ok_reports += 1


print(ok_reports)





    
    




