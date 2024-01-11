from opcoes.alterar import alterar_aluno
from opcoes.buscar import buscar_aluno
from opcoes.cadastrar import cadastrar_aluno
from opcoes.excluir import excluir_aluno
from opcoes.resumir import resumir_aluno
from opcoes.sair import sair
from uteis.menu import menu

print("\nCADASTRO DE ALUNOS\n")

menu()

escolhas = ["1", "2", "3", "4", "5", "6"]

alunos = []

# acesso ao menu
while True:

    # validacao da entrada
    while True:
        opcao = input("Escolha uma opcao: ")
        if opcao.isnumeric() and opcao in escolhas:
            break
    # validacao da entrada

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        resumir_aluno()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        alterar_aluno()
    elif opcao == "5":
        excluir_aluno()
    else:
        sair()
# acesso ao menu