salario = float(input("Digite seu salario atual: "))

if salario > 1250:
    aumento = 10/100 # 10%
    salario = salario + (salario*aumento)
    print(f"Parabens seu salario agora é de R$ {salario} reais")

if salario <= 1250:
    aumento = 15/100 # 15%
    salario = salario + (salario*aumento)
    print(f"Parabens seu salario agora é de R$ {salario} reais")
