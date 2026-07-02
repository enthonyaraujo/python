salario = float(input("Digite o valor do salário: "))
aumento = (float(input("Digite o valor do aumento: ")))/100
aumento_total = salario * aumento
novo_salario = salario + aumento_total

print(f"Seu novo salário será de: R$ {novo_salario} reais, que teve um aumento de R$ {aumento_total} reais")