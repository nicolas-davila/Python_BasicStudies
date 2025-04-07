"""Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os 
quais fornece a quantidade de ração em gramas. A quantidade diária de ração 
fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do 
saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre 
quanto restará de ração no saco após cinco dias. """

feed_bag = float(input("Digite o peso do saco de ração em kg: "))
cat_count = int(input("Digite a quantidade de gatos em casa: "))
daily_amount = float(input("Digite a quantidade fornecida para os gatos em g: "))

full_bag = feed_bag*1000

daily_amount_feed = 0

for day in range(5):
    daily_amount_feed += (daily_amount*cat_count)

remaining_quantity = (full_bag - daily_amount_feed)/1000

print(f"A quantidade restante é de: {remaining_quantity:.2f}Kg")
