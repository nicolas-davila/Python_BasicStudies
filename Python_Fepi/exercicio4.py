'''4. Ler dois valores de duas variáveis x e y e realizar a troca dos valores, após a troca, 
imprimir na tela os novos valores das variáveis x e y. '''

x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))

# x_value = x # salva o primeiro valor digitado de x
# x = y # troca o valor de x
# y = x_value # troca o valor de y

x, y = y, x # realiza a troca dos valores de forma mais elegante

print(f"O valor do 1° número digitado agora é: {x}")
print(f"O valor do 2° número digitado agora é: {y}")

