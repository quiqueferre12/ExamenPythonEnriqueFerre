
import csv

directorio=("D://Universidad3Curso//examen_python_EnriqueFerreCarbonell//ExamenPythonEnriqueFerre//winequality.csv")

def read_data(fichero):
    with open(fichero,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_data(directorio)


