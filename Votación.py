#Votación
#Se realizó una votación con 30 candidatos identificados con un número del 1 al 30. 5000 estudiantes votaron; 
#imprima de mayor a menor según el número de votos.
#Juan José Calderón Gómez

import numpy as np


votos = np.random.randint(1,31,5000)

conteo = np.bincount(votos)

candOrd = np.argsort(conteo)[::-1]

print("Los resultados de la elección del representante de los estudiantes al consejo superior fueron:\n")
for i in candOrd:

    if i!= 0 :
        print(f"Candidato #{i}: {conteo[i]}")

