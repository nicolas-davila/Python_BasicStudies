'''5. Criar um programa que lê o tamanho do lado de um quadrado e 
calcule sua área (lado*lado) e seu perímetro (lado*4) e imprima na tela. '''

side_square = float(input("Digite o tamanho do lado do quadrado em metros: "))

area = side_square * side_square
perimeter = side_square * 4

print(f"A área do quadrado é de: {area:.2f} m²")
print(f"O perímetro do quadrado é de: {perimeter:.2f} m")