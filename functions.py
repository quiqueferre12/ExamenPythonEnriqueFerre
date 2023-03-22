
import csv

directorio=("D://Universidad3Curso//examen_python_EnriqueFerreCarbonell//ExamenPythonEnriqueFerre//winequality.csv")

def read_data(fichero):
    dic={}
    cont=1
    nombre="dato"
    with open(fichero,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row)==13:
                var=nombre+str(cont)
                dicaux ={ "type": row[0],"fixed acidity": row[1], "volatile acidity": row[2], "citric acidity": row[3], "residual sugar": row[4],
                       "chlorides": row[5], "free sulfur dioxide": row[6], "total sulfur dioxide": row[7],
                       "density":row[8], "PH":row[9], "sulphates": row[10], "alcohol": row[10], "quality":row[11]} 
                dic.update({var:dicaux}) 
                cont=cont+1
    return dic

def split(diccionario):

    dicRed={}
    dicWhite={}
    for i in diccionario:
        if diccionario[i]["type"] == "red":
            print (diccionario[i])
            diccionario[i].pop("type")
            dicRed.update(diccionario[i])
        else:
            diccionario[i].pop("type")
            dicWhite.update(diccionario[i])
    return dicRed, dicWhite



dicionario =read_data(directorio)
dicRojo,dicBlanc =split(dicionario)
print(dicRojo)


