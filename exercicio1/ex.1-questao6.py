print("Bem-vindo ao sistema!")
print("Veja as opções abaixo e em seguida escolhar uma opção: ")
print(" 1. Cadastrar alunos \n 2.Consultar aluno \n 3. Alterar aluno \n 4. Excluir aluno \n 5. Listar alunos \n 6. Sair")

while True:
    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            nome = "Cadastrar aluno"
            print(nome)
        case 2:
            nome = "Consultar aluno"
            print(nome)
        case 3:
            nome = "Alterar aluno"
            print(nome)
        case 4:
            nome = "Excluir aluno"
            print(nome)
        case 5:
            nome = "Listar alunos"
            print(nome)
        case 6:
            nome = "Sair"
            print(nome)
            break
        case _:
            nome = "Opção inválida"
            print(nome)