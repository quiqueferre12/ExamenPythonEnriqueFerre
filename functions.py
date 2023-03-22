
import csv


with open("winequality.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

f = open("winequality.csv", mode="rt", encoding="utf-8")
lista_lineas = f.readlines()
    
for i in range(len(lista_lineas)):
        
    print("Lista de líneas leídas: ", lista_lineas[i])
        
f.close()
