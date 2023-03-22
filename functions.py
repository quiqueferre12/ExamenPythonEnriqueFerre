
def read_data(fichero):
    f = open(fichero+".csv", mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    mayor=lista_lineas[0]
    for i in range(len(lista_lineas)):
        print("Lista de líneas leídas: ", lista_lineas[i])

read_data("winequality")
