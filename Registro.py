#Registro
#En la UIS hay 6500 estudiantes, para los cuales tenemos registrado su código, nombre y promedio acumulado;
#Imprima el código y nombre de los estudiantes de la carrera X con promedio acumulado mayor a 4 y el total de estos;
#Imprima el código y nombre de los estudiantes que ingresaron antes de 1980 y están condicionales.

import numpy as np
import random as rn
import requests 

class estudiante:

    def __init__(self, name, code, average, degree, year):

        self.name = name
        self.code = code
        self.average = average
        self.degree = degree
        self.year = year

print('\t\tBase de Datos UIS')

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co&content-type=text%2Fplain'
datos = requests.get(url)
texto = datos.text
palabras = texto.split()

degrees = {10 : 'Biología', 11 : 'Ing. de Sistemas', 14 : 'Química', 16 : 'Lic. en Matemáticas', 18 : 'Física',
            21 : 'Ing. Civil', 22 : 'Ing. Eléctrica', 23 : 'Ing. Industrial', 24 : 'Ing. Mecánica', 
            26 : 'Ing. Electrónica', 27: 'Diseño Industrial', 30: 'Lic. en Música',31 : 'Ing. Metalúrgica', 32 : 'Ing. de Petroleos',
            33 : 'Ing. Química', 34 : 'Geología', 37 : 'Filosofía', 39 : 'Matemáticas',
            41 : 'Trabajo Social', 45 : 'Economía', 46 : 'Derecho', 51 : 'Enfermería', 52 : 'Medicina',56 : 'Fisioterapia', 
            57 : 'Nutrición y Dietética', 58 : 'Microbiología y Bioanálisis', 60 : 'Historia y Archivistica',
            63 : 'Lic. en Lenguas con Enfásis en Inglés', 64 : 'Lic. en Literatura y LC', 68 : 'Lic. en Educ. Básica Primaria'}

degreesNum = np.array([10, 11, 14, 16, 18, 21, 22, 23, 24, 26, 27, 30, 31, 32, 33, 34, 
              35, 37, 39, 41, 45, 46, 51, 52, 56, 57, 58, 60, 63, 64, 68])

estudiantes = []

for i in range(6501):

    palabraNum = rn.randint(0, len(palabras)-1)
    nombre = palabras[palabraNum]
    codigo = rn.randint(2220000, 2229999)
    promedio = rn.uniform(2.7, 5.0)
    promedioR = round(promedio, 2)
    degreesRand = rn.randint(0, len(degreesNum)-1)
    degreesKey = degreesNum[degreesRand]
    carrera = degrees.get(degreesKey)
    año = rn. randint(1948, 2023)
    j = estudiante(nombre, codigo, promedioR, carrera, año)

    estudiantes.append(j)

print('\nIngrese el número de la carrera correspondiente: ')
crr = int(input())
print(f'\nLos estudiantes con promedio mayor que 4.0 de la carrera de {degrees.get(crr)} son:')
estProm = 0

for i in range(6501):

    if estudiantes[i].degree == degrees.get(crr) and estudiantes[i].average > 4.0 :

        estProm = estProm + 1 
        print(f'\nNombre: {estudiantes[i].name}, Código: {estudiantes[i].code}, Promedio: {estudiantes[i].average}, Carrera: {estudiantes[i].degree}')

print(f'\nLa cantidad de estudiantes con promedio mayor que 4.0 de la carrera de {degrees.get(crr)} son: {estProm}' )

print('\nLos estudiantes que ingresaron antes de 1980 y están condicionales son: ')

for i in range(6501):

    if estudiantes[i].year < 1980 and (estudiantes[i].average >= 2.7 and estudiantes[i].average <= 3.2):

        print(f'\nNombre: {estudiantes[i].name}, Código: {estudiantes[i].code}, Año: {estudiantes[i].year}, Promedio: {estudiantes[i].average}')
