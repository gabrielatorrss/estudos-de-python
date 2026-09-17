#entrada de dados
media_escolar = float(input("Digite sua média escolar: "))
frequencia = float(input("Digite sua porcentagem de frequencia em %: "))
renda = float(input("Digite sua renda familiar: R$ "))
bolsa_externa = input("Você já tem outra bolsa? (s/n): ")

#processamento de dados
motivos = []

if media_escolar >= 7 and frequencia >= 75 and renda <= 3000 and bolsa_externa in ("n", "N"):
    classificacao = "elegível!"
else:
    if media_escolar < 7:
        motivos.append("média insuficiente")
    if frequencia < 75:
        motivos.append("frequência insuficiente")
    if renda > 3000:
        motivos.append("renda acima do limite.")
    if bolsa_externa in ("s", "S"):
        motivos.append("já possue outra bolsa")
    classificacao = (f"não elegível! \nMotivo(s): {', '.join(motivos)}")

#saída de dados 
print(f"O status da sua aplicação para a bolsa é: {classificacao}")