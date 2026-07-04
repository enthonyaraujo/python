distancia = float(input("Qual a distancia em km que deseja percorrer? "))

if distancia <= 200:
    passagem = 0.50
    preco = passagem * distancia

else:
    passagem = 0.45
    preco = passagem * distancia

print(f"valor total da viagem: R$ {preco}")
 


