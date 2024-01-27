def processa_notificacoes(num_notificacoes, notificacoes):
    livro_ofertas = []
    for i in range(num_notificacoes):
        posicao, acao, valor, quantidade = notificacoes[i]
        if acao == 0:  # Inserir
            livro_ofertas.insert(posicao - 1, [valor, quantidade])
        elif acao == 1:  # Modificar
            if quantidade == 0:
                livro_ofertas[posicao - 1][0] = valor
            else:
                livro_ofertas[posicao - 1] = [valor, quantidade]
        elif acao == 2:  # Deletar
            del livro_ofertas[posicao - 1]
    return [[i+1] + oferta for i, oferta in enumerate(livro_ofertas)]

num_notificacoes = 12
notificacoes = [
    [1, 0, 15.4, 50],
    [2, 0, 15.5, 50],
    [2, 2, 0, 0],
    [2, 0, 15.4, 10],
    [3, 0, 15.9, 30],
    [3, 1, 0, 20],
    [4, 0, 16.50, 200],
    [5, 0, 17.00, 100],
    [5, 0, 16.59, 20],
    [6, 2, 0, 0],
    [1, 2, 0, 0],
    [2, 1, 15.6, 0]
]

livro_ofertas = processa_notificacoes(num_notificacoes, notificacoes)
livro_ofertas  # Retorna o livro de ofertas atualizado
