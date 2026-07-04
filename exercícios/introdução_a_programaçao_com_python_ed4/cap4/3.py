a = int(input("Digite o primeiro valor: "))

b = int(input("Digite o segundo valor: "))

c = int(input("Digite o terceiro valor: "))

if a > b and a > c:
    maior = a
    if b > c:
        menor = c
    if b < c:
        menor = b
    print(f"Maior: {maior}, Menor: {menor}")


if b > a and b > c:
    maior = b
    if a > c:
        menor = c
    if a < c: 
        menor = a
    print(f"Maior: {maior}, Menor: {menor}")

if c > b and c > a:
    maior = c
    if b > a:
        menor = a 
    if b < a:
        menor = b
    print(f"Maior: {maior}, Menor: {menor}")





