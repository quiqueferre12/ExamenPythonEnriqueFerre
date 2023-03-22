import functions
directorio=("D://Universidad3Curso//examen_python_EnriqueFerreCarbonell//ExamenPythonEnriqueFerre//winequality.csv")#he tenido que poner esto porque no me detectaba mi archivo csv

diccionario=functions.read_data(directorio)
dicRojo,dicBlanc =functions.split(diccionario)
lista=functions.reduce(dicRojo,"PH")
print(len(dicRojo))
print(len(dicBlanc))
