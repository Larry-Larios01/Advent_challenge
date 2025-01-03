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




def get_source() -> str:
    # URL de la página
    url = "https://adventofcode.com/2024/day/2/input"

    # Realizar solicitud HTTP

    session = os.getenv("SESSION")
    cookies = {'session': session}

    response = requests.get(url, cookies=cookies)
    return response.text


def get_list_of_source(source: str) -> list[str]:
    text_strip = source.strip().split("\n")
    for item in text_strip:
        splitted = item.split()
        print(splitted)

    return splitted
        




def iter_the_individual_list(source: str) -> int:
    acumulate = 0
    response_of_checker: bool
    text_strip = source.strip().split("\n")
    for item in text_strip:
        splitted = item.split()
        print(splitted)
        response_of_checker = check_list(splitted, lenght= len(splitted))
        if response_of_checker:
            acumulate += 1



    return acumulate


def check_list(list:list[str], safe:bool = False, acc: int = -1, lenght = 0):
    if acc == -1:
        ll = fill_the_linked_list(list)
        safe = is_safe(ll)
    if acc != -1:
        temp_list = list[:]
        del temp_list[acc]
        ll = fill_the_linked_list(temp_list)
        safe = is_safe(ll)



    if safe == True or len(list) == acc+1:
        return safe
    
    return check_list(list, safe, acc+1)
    

def fill_the_linked_list( list: list[str])-> LinkedList:
        ll = LinkedList()
        for split in list:
            ll.insert_at_end(split)

        return ll




    
def is_safe(ll: LinkedList):
    current = ll.head
    incre_decre = ""
    while current: 
        next_node = ll.find_next_node(current)

        print("teh next node", next_node)
        if next_node:
            result = abs(current.data-next_node.data)
            if current.data> next_node.data:
                if incre_decre == "i":
            
                    return False
                    
                    
                elif incre_decre is not "i":
                    incre_decre = "d"

            if current.data < next_node.data:
                if incre_decre == "d":

                    return False
                    
                    
                elif incre_decre is not "d":
                    incre_decre = "i"
            if result < 1 or result>3:
                    return False
                    
                
            current = current.next
            print("the current", current.data)
        if not next_node:
            return True
        








   

    





if __name__ == "__main__":
    source = get_source()
    #list_of_source = get_list_of_source(source)
    response2 = """
1 2 7 8 9
7 6 4 2 1
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9 
"""   
    results = iter_the_individual_list(source) 
    print("teh results are", results)


    

    







 




