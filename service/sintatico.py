#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:33:12 2022

@author: marlonoliveira
"""
import numpy as np

#entrada, geralmente vem de um arquivo texto
#palavra = 'void main { inicio ; fim }'

#variavel para armazenar o lexema 
#lexema = ''

#variavel para armazenar a lista de tokes (que ira alimentar o sintatico)
tokens = [2, 11, 39, 15, 40, 20, 38]

        
print(tokens) # [2, 11, 39, 15, 40, 20, 38]
tokens = np.array(tokens)

#gramatica
producoes = [[  2, 11, 39, 52, 53, 54, 38 ]] #P1
producoes = np.append(producoes, [[ 0, 0, 0, 0, 0, 0, 0]], axis = 0); #P2
producoes = np.append(producoes, [[ 17, 0, 0, 0, 0, 0, 0]], axis = 0); #P3
producoes = np.append(producoes, [[ 15, 65, 40, 66, 20 , 0, 0]], axis = 0); #P4 
producoes


tabParsing = np.zeros((82, 50))

tabParsing[51][2] = 1
tabParsing[52][15] = 3
tabParsing[53][15] = 3 # pela tab de parsing seria 19, simplificando para 3 pq eh igual
tabParsing[54][15] = 4 # pela tab de parsing seria 31, simplificando para 4
tabParsing[65][40] = 3 # pela tab de parsing seria 38, simplificando para 3 pq eh igual
tabParsing[66][20] = 3 # pela tab de parsing seria 32, simplificando para 3 pq eh igual

pilha = [47] #$

pilha = np.hstack([producoes[0][:], pilha])

print(pilha)


X = pilha[0]
a = tokens[0]

while X != 47 : #$
    print(X)
    print(a)
    print(pilha) #obrigatorio mostrar a pilha a cada iteracao
    if X == 17: # vazio
        pilha = np.delete(pilha,[0])
        X = pilha[0]
    else:
        if X <= 50: # x é terminal
            if X == a:
                pilha = np.delete(pilha,[0])
                tokens = np.delete(tokens,[0])
                X = pilha[0]
                if tokens.size != 0:
                    a = tokens[0]
            else:
                print('Error')
                break
        else: # nao terminal
            topo = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha])
            if topo[0] == 17: # vazio
                X = topo[0]
            else: # topo nao tem vazio
                if topo[0] != 0:  
                    pilha = np.delete(pilha,[0])
                    pilha = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha]) #consulta tab parsinal e empilha a producao referente
                    pilha = pilha[pilha != 0]
                    X = pilha[0]
                    #print('aqui')
                else:
                    print('Error')
                    break
        
        