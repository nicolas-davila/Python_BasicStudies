'''6 – Criar um programa que calcule e mostre o volume de uma esfera. 
A fórmula para o cálculo é:

4/3∗pi∗raio
 
Podem verificar como importar bibliotecas (se quiserem) e importar a biblioteca math, 
que possui a variável Pi. Caso contrário, podem utilizar o valor de Pi como 3.1415 '''

import math

radius = float(input("Digite o valor do raio da esfera em cm: "))

volume = (4/3) * math.pi * (radius ** 3)

print(f"O volume da esfera é de: {volume:.2f}cm³")