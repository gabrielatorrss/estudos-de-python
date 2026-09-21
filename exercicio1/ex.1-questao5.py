# entrada de dados
produtividade = float(input("Digite sua nota de produtividade: "))
qualidade = float(input("Digite sua nota de qualidade: "))
presença = float(input("Digite seu percentual de presença(%): "))

#processamento de dados
media = float((produtividade + qualidade) / 2)

if presença < 75: 
    classificacao = "Desempenho comprometido por baixa frequência"
elif media >= 9 and presença >= 90:
    classificacao = "Excelente"
elif media >= 7 and presença >= 85:
    classificacao = "Bom"
elif media >= 5 and presença >= 75:
    classificacao = "Regular"
else:
    classificacao = "Insatisfatório"

# saída de dados
print(f"Seu resultado de desempenho é: {classificacao}!")