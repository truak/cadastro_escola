def resumir_aluno(lista, nome):

    d = {}
    media = 0.0

    for d in lista:
        if d['Nome'] == nome.upper():
            media = (d['Nota1'] + d['Nota2'] + d['Nota3'] + d['Nota4']) / 4
            break

    print(f"""
          Aluno: {nome.upper()}
          Disciplina: {d['Disciplina']}
          Notas: {d['Nota1'], d['Nota2'], d['Nota3'], d['Nota4']}
          Média: {media}
          Situação: {'Aprovado(a)' if media >= 7 else 'Reprovado(a)'}
          """)
