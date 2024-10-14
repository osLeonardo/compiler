import numpy as np

def sintatico(token_array):
    # Variável para armazenar o array de tokens (que irá alimentar o sintático)
    tokens = np.array(token_array)

    # Gramática
    producoes = [[9, 16, 42, 54, 46]]  # P0: <PROGRAMA> ::= "program" "identificador" ";" <BLOCO> "."
    producoes = np.append(producoes, [[55, 56, 57, 58]], axis=0)  # P1: <BLOCO> ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    producoes = np.append(producoes, [[23, 16, 31, 59, 42, 60]], axis=0)  # P2: <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    producoes = np.append(producoes, [[17]], axis=0)  # P3: <DCLCONST> ::= î (epsilon)
    producoes = np.append(producoes, [[16, 31, 59, 42, 60]], axis=0)  # P4: <LDCONST> ::= "identificador" "=" <TIPO> ";" <LDCONST>
    producoes = np.append(producoes, [[17]], axis=0)  # P5: <LDCONST> ::= î (epsilon)

    tabParsing = np.zeros((82, 50))

    # Exemplo de preenchimento da tabela de parsing
    tabParsing[53][9] = 1  # Estado <PROGRAMA>, token "program" -> Produção 0
    tabParsing[54][23] = 2  # Estado <BLOCO>, token "const" -> Produção 2
    # Continue preenchendo a tabela conforme necessário

    pilha = [51]  # $

    pilha = np.hstack([producoes[0][:], pilha])

    print(pilha)

    X = pilha[0]
    a = tokens[0]

    while X != 51:  # $
        print(X)
        print(a)
        print(pilha)  # Obrigatório mostrar a pilha a cada iteração
        if X == 17:  # Vazio
            pilha = np.delete(pilha, [0])
            X = pilha[0]
        else:
            if X <= 52:  # X é terminal
                if X == a:
                    pilha = np.delete(pilha, [0])
                    tokens = np.delete(tokens, [0])
                    X = pilha[0]
                    if tokens.size != 0:
                        a = tokens[0]
                else:
                    print('Error')
                    break
            else:  # Não terminal
                topo = np.hstack([producoes[int(tabParsing[X][a]) - 1][:], pilha])
                if topo[0] == 17:  # Vazio
                    X = topo[0]
                else:  # Topo não tem vazio
                    if topo[0] != 0:
                        pilha = np.delete(pilha, [0])
                        pilha = np.hstack([producoes[int(tabParsing[X][a]) - 1][:], pilha])  # Consulta tab parsing e empilha a produção referente
                        pilha = pilha[pilha != 0]
                        X = pilha[0]
                    else:
                        print('Error')
                        break