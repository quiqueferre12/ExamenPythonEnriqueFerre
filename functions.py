from functools import reduce
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
    contred=1
    contwhite=1
    dicWhite={}
    for i in diccionario:
        if diccionario[i]["type"] == "red":
            diccionario[i].pop("type")
            dicRedaux={ diccionario[i]["fixed acidity"],diccionario[i]["volatile acidity"],diccionario[i]["citric acidity"],diccionario[i]["residual sugar"],diccionario[i]["chlorides"],
                       diccionario[i]["free sulfur dioxide"],diccionario[i]["total sulfur dioxide"],diccionario[i]["density"],diccionario[i]["PH"],diccionario[i]["sulphates"],diccionario[i]["alcohol"]
                       ,diccionario[i]["quality"]}
            dicRed.update({"dato"+str(contred):dicRedaux})
            contred=contred+1
        elif diccionario[i]["type"] == "white":
            diccionario[i].pop("type")
            dicRedaux={ diccionario[i]["fixed acidity"],diccionario[i]["volatile acidity"],diccionario[i]["citric acidity"],diccionario[i]["residual sugar"],diccionario[i]["chlorides"],
                       diccionario[i]["free sulfur dioxide"],diccionario[i]["total sulfur dioxide"],diccionario[i]["density"],diccionario[i]["PH"],diccionario[i]["sulphates"],diccionario[i]["alcohol"]
                       ,diccionario[i]["quality"]}
            dicWhite.update({"dato"+str(contwhite):dicRedaux})
            contwhite=contwhite+1

    return dicRed, dicWhite


def reduce(dic,string):
    listares=[]
    for i in dic:
        if dic[i][string]==string:
            listares.insert(dic[i][string])
            print(listares)
    return listares

    




