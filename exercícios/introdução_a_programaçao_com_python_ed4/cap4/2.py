velocidade = float(input("Velocidade: (Km/h) "))

if velocidade > 80:
    multa = 80*5
    print(f"Voce foi multado em R$ {multa}. ")
if velocidade <=80:
    print("Parabens esta dirigindo na velocidade correta ")
