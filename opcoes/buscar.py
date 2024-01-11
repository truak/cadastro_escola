def buscar_aluno():

    d = {}
    msg = 'Aluno não cadastrado'

    lista = list(input("Banco de dados: "))
    nome = input("Aluno: ")

    for d in lista:
        if d['Nome'] == nome.upper():
            msg = 'Aluno cadastrado'
            break

    print(msg)
