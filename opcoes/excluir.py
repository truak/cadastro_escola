def excluir_aluno():

    d = {}

    lista = list(input("Banco de dados: "))
    nome = input("Aluno: ")

    for d in lista:
        if d['Nome'] == nome.upper():
            lista.remove(d)
            break

    print("\nCadastro excluido\n")
