import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# URL de la página
url = "https://adventofcode.com/2024/day/1/input"

# Realizar solicitud HTTP

session = os.getenv("SESSION")
cookies = {'session': session}

response = requests.get(url, cookies=cookies)

#print(response.text)

text_strip = response.text.strip().split("\n")

valores = []


i = 1
left = []
right = []
for line in text_strip:
    splitted = line.split()
    left.append(int(splitted[0]))
    right.append(int(splitted[1]))



left.sort()
right.sort()

len(right)
len(left)

#def result_recursion(i=0, acc=0):

    #if len(left) ==i:
        #return acc
    
    #result = abs(left[i]-right[i])


    #return(result_recursion(i+1, acc+result))

result = 0

for i in range(len(left)):
    result += abs(left[i]-right[i])

print(result)



resultado = 0
for i in range(len(left)):
    if left[i] not in right:
        resultado += 0
    j = 0
    if left[i] in right:
        for item in right:
            if item == left[i]:
                j+=1
        resultado += left[i]*j


print(resultado)


