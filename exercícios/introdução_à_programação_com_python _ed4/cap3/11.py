preço_atual = float(input("Valor atual do produto sem desconto: "))
desconto = (float(input("Desconto de: ")))/100
valor_descontado = preço_atual*desconto
preço_com_desconto = preço_atual - valor_descontado 

print(f"Valor do Produto: R$ {preço_com_desconto}, com desconto de: R$ {valor_descontado}")