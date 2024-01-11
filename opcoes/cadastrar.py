def cadastrar_aluno():

    d = {}

    lista = list(input("Banco de dados: "))
    nome = input("Aluno: ")
    disciplina = input("Disciplina: ")
    nota1 = input("Nota 1: ")
    nota2 = input("Nota 2: ")
    nota3 = input("Nota 3: ")
    nota4 = input("Nota 4: ")

    d['Nome'] = nome.upper()
    d['Disciplina'] = disciplina.upper()
    d['Nota1'] = nota1
    d['Nota2'] = nota2
    d['Nota3'] = nota3
    d['Nota4'] = nota4

    print("\nAluno cadastrado\n")
    
    return lista.append(d)
