#entrada de dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
experiencia = int(input("Digite seu tempo de experiência de trabalho em anos: "))
valor_solicitado = float(input("Digite o valor do empréstimo que deseja solicitar: R$ "))

#processamento de dados
motivos = []
valor_elegivel = salario * 10

if idade >= 18  and salario >= 1500 and experiencia >= 1 and valor_solicitado <= valor_elegivel: 
    classificacao = "Empréstimo pré-aprovado!"
else:
    if idade < 18:
        motivos.append("empréstimo não permitido para menores de idade")
    if salario < 1500:
        motivos.append("renda insuficiente")
    if experiencia < 1:
        motivos.append("tempo de trabalho insuficiente")
    if valor_solicitado > valor_elegivel:
        motivos.append("valor solicitado muito alto")
    classificacao = (f"não elegível! \nMotivos: {', '.join(motivos)}")

#saída de dados
print(f"O status da sua solicitação do empréstimo é: {classificacao}")

