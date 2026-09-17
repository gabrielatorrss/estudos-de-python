# entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade? Digite em números: "))

#processamento de dados 
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Inválida"

#saída de dados
print (f"{nome}, você é classificado(a) como: {categoria}") 
