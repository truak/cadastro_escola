def alterar_aluno(lista, nome, disciplina, nota1, nota2, nota3, nota4):

    d = {}

    for d in lista:
        if d['Nome'] == nome.upper():
            d['Disciplina'] = disciplina.upper()
            d['Nota1'] = nota1
            d['Nota2'] = nota2
            d['Nota3'] = nota3
            d['Nota4'] = nota4
            break

    print("\nCadastro alterado\n")
    