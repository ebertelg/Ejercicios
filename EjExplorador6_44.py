# -*- coding: utf-8 -*-
"""EjExplorador6_44.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ae6AO3nprVyeCTrMxHcGoX2JDdsRngzC
"""

#Puntaje final
respuestas_correctas = int(input("Ingrese el número de respuestas correctas: "))
respuestas_incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
respuestas_en_blanco = int(input("Ingrese el número de respuestas en blanco: "))

puntaje_final = (respuestas_correctas * 3) + (respuestas_incorrectas * -1)
print(f"El puntaje final es: {puntaje_final}")