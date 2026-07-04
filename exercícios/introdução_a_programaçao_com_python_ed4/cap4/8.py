a = int(input("Digite o valor de 'a':  "))
b = int(input("Digite o valor de 'b':  "))

opcao = int(input("Qual operação deseja realizar? \n1. +\n2. -\n3. *\n4. /\n> "))

if opcao == 1:
    operacao = "+"
    resultado = a + b
elif opcao == 2:
    operacao = "-"
    resultado = a - b
elif opcao == 3:
    operacao = "*"
    resultado = a * b
elif opcao == 4:
    operacao = "/"
    resultado = a / b
else:
    print("Opcao Invalida")

print(f"Resultado de {a} {operacao} {b} = {resultado}")