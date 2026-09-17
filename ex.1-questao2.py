#entrada de dados
produto = input ("Qual é o produto? ")
preco = float(input(f"Qual o preço do {produto}? R$ "))
quantidade = int(input(f"Qual a quantidade do {produto} em estoque? "))

#processamento de dados 
if quantidade < 0:
    classificacao = "Quantidade de estoque inválida"
elif preco <= 0:
    classificacao = "Preço inválido"
elif preco > 1000 and quantidade < 5:
    classificacao = "Produto caro com estoque crítico"
elif preco > 1000 and quantidade >= 5 and quantidade <= 20:
    classificacao = "Produto caro com estoque normal"
elif preco > 1000 and quantidade > 20:
    classificacao = "Produto caro com estoque alto"
elif preco <= 1000 and quantidade < 5:
    classificacao = "Estoque crítico"
else:
    classificacao = "estoque normal"

# saída de dados
print(f"O {produto} está classificado como: {classificacao}")
