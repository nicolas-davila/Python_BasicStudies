first_value = int(input("Digite o primeiro valor: "))
second_value = int(input("Digite o segundo valor: "))

soma = first_value + second_value

if soma > 20:
    soma += 8
else:
    soma -= 5

print(f"A soma é: {soma}")
    