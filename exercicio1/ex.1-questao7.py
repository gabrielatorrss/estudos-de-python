#entrada de dados

print("\n============== SISTEMA DE MATRÍCULA ==============\n")

nome = input("\n[DIGITE SEU NOME COMPLETO]: \n")
idade = int(input("\n[DIGITE SUA IDADE]: \n"))
media = float(input("\n[DIGITE SUA MÉDIA]: \n"))
frequencia = int(input("\n[DIGITE SEU PERCENTUAL DE FREQUÊNCIA]: \n"))

#processamento

print("\n[TIPO DE CURSO]\n\n1 – Graduação\n2 – Técnico\n3 – Pós-graduação")
curso = int(input("\n[ESCOLHA UMA OPÇÃO]: "))

while curso < 1 or curso > 3:
    print("\n[NÚMERO INVÁLIDO]\n[TENTE NOVAMENTE]\n")
    curso = int(input("\n[ESCOLHA UMA OPÇÃO]: "))

match curso:

    case 1:

        if frequencia < 75:
            print("\n\n[REPROVADO]\n\n")

        elif media >= 7:
            print("\n\n• Graduação - [APROVADO]\n\n")
        elif media >= 5:
            print("\n\n• Graduação - [RECUPERAÇÃO]\n\n")
        else:
            print("\n\n• Graduação - [REPROVADO]\n\n")

    case 2:

        if frequencia < 75:
            print("\n\n[REPROVADO]\n\n")

        elif media >= 6:
            print("\n\n• Técnico - [APROVADO]\n\n")
        elif media >= 4:
            print("\n\n• Técnico - [RECUPERAÇÃO]\n\n")
        else:
            print("\n\n• Técnico - [REPROVADO]\n\n")

    case 3:
            
        if frequencia < 75:
                print("\n\n[REPROVADO]\n\n")

        elif media >= 7:
                print("\n\n• Pós-Graduação - [APROVADO]\n\n")
        else:
                print("\n\n• Pós-Graduação - [REPROVADO]\n\n")

print("============== FIM ==============\n\n")