name = input("Digite seu nome: ")
first_exam = float(input("Digite a nota da primeira prova: "))
second_exam = float(input("Digite a nota da segunda prova: "))
final_work = float (input("Digite a nota do trabalho final: "))

media = (first_exam + second_exam + final_work) / 3

if media > 6:
    print(f"{name} Aprovado!")
    print(f"Média: {media:.2f}")
elif media < 3:
    print(f"{name} Reprovado!")
    print(f"Média: {media:.2f}")
else:
    print(f"{name} em Recuperação!")
    print(f"Média: {media:.2f}")