cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fumou? "))
minutos_perdidos = 10
dias_perdidos = (cigarros_dia * minutos_perdidos * 365 * anos) / (24*60)

print("Você perderá: %d dias" % dias_perdidos) 