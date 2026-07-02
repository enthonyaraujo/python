dias_para_segundos = (float(input("Digite a quantidade de dias: ")))*129600
horas_para_segundos = (float(input("Digite a quantidade de horas: ")))*3600
minutos_para_segundos = (float(input("Digite a quantidade de minutos: ")))*60
segundos = float(input("Digite a quantidade de segundos: "))

total = dias_para_segundos+horas_para_segundos+minutos_para_segundos+segundos

print(f"total = {total} segundos")