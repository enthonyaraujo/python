dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
km = float(input("Digite a quantidade de km percorridos com o carro: "))

dias = dias*60
km = km*0.15
total = dias + km

print("Valor a pagar: %.2f" % total)