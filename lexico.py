import numpy as np

with open('exemplo01.txt', 'r') as arquivo:
    palavra = arquivo.read()

tokens = []
lexemas = []
lines = []
espacos = [' ', '\n', '\t', '\r']
simbolos = ['>=', '>', '=', '<>', '<=', '<', '+', ']', '[', ';', ':', '/', '..', '.', ',', '*', ')', '(', '-']
reservados = ['write', 'while', 'until', 'to', 'then', 'string', 'repeat', 'real', 'read', 'program',
              'procedure', 'or', 'of', 'integer', 'if', 'for', 'end', 'else', 'do', 'declaravariaveis',
              'const', 'char', 'chamaprocedure', 'begin', 'array', 'and']

lexema = ''
currentLine = 1
lineComment = False;
blockComment = False;
literalLimiter = False;
charLimiter = False;
strLimiter = False;
numLimiter = False;

for i in range(len(palavra)):
    if palavra[i] == '\n':
        currentLine += 1
        lineComment = False

    elif palavra[i] == '_':
        if literalLimiter:
            lexema = lexema + palavra[i]
            tokens.append(13)
            lines.append(currentLine)
            lexemas.append(lexema)
            strLimiter = False
            charLimiter = False
            literalLimiter = False
            print(lexema)
            lexema = ''
        else:
            lexema = lexema + palavra[i]
            literalLimiter = True

    elif palavra[i] == '"':
        if strLimiter:
            if len(lexema) > 11:
                print(f'Erro: String não pode ter mais de 10 caracteres. Linha: {currentLine}')
                break
            lexema = lexema + palavra[i]
            tokens.append(38)
            lines.append(currentLine)
            lexemas.append(lexema)
            strLimiter = False
            charLimiter = False
            literalLimiter = False
            print(lexema)
            lexema = ''
        else:
            lexema = lexema + palavra[i]
            strLimiter = True

    elif palavra[i] == "'":
        if charLimiter:
            if len(lexema) > 2:
                print(f'Erro: Char não pode ter mais de um caractere. Linha: {currentLine}')
                break
            else:
                lexema = lexema + palavra[i]
                tokens.append(39)
                lines.append(currentLine)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                print(lexema)
                lexema = ''
        else:
            lexema = lexema + palavra[i]
            charLimiter = True

    elif palavra[i].isdigit():
        if numLimiter:
            if palavra[i+1].isdigit() or (palavra[i+1] == '.' and '.' not in lexema):
                lexema = lexema + palavra[i]
            else:
                lexema = lexema + palavra[i]
                if '.' in lexema:
                    parts = lexema.split('.')
                    if len(parts[0]) > 5:
                        print(f'Erro: Número real não pode conter mais de 5 dígitos antes do divisor. Linha: {currentLine}')
                        break
                    elif len(parts[1]) > 2:
                        print(f'Erro: Número real não pode conter mais de 2 dígitos após do divisor. Linha: {currentLine}')
                        break
                    else:
                        tokens.append(36)
                        lines.append(currentLine)
                else:
                    if len(lexema) > 5:
                        print(f'Erro: Número inteiro não pode conter mais de 5 dígitos. Linha: {currentLine}')
                        break
                    else:
                        tokens.append(37)
                        lines.append(currentLine)
                lexemas.append(lexema)
                print(lexema)
                lexema = ''
                numLimiter = False
        else:
            lexema = lexema + palavra[i]
            numLimiter = True

    elif palavra[i].isalpha():
        lexema = lexema + palavra[i]

        if lexema in reservados and (palavra[i+1] in espacos or palavra[i+1] in simbolos):
            tokens.append(reservados.index(lexema))
            lines.append(currentLine)
            lexemas.append(lexema)
            print(lexema)
            lexema = ''

        elif len(lexema) > 10:
            print(f'Erro: Identificador não pode ter mais de 10 caracteres. Linha: {currentLine}')
            break

        elif palavra[i+1] in espacos or palavra[i+1] in simbolos:
            tokens.append(16)
            lines.append(currentLine)
            lexemas.append(lexema)
            print(lexema)
            lexema = ''

    elif palavra[i] in simbolos:
        if lexema:
            if lexema in reservados:
                tokens.append(reservados.index(lexema))
            else:
                tokens.append(16)
            lines.append(currentLine)
            lexemas.append(lexema)
            lexema = ''

        tokens.append(simbolos.index(palavra[i]) + 29)
        lines.append(currentLine)
        lexemas.append(palavra[i])
        lexema = ''

    elif palavra[i] in espacos:
        if lexema:
            if lexema in reservados:
                tokens.append(reservados.index(lexema))
            else:
                tokens.append(16)
            lines.append(currentLine)
            lexemas.append(lexema)
            lexema = ''

for i in range(0,len(tokens)):
    print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: ' +str(lines[i]))

tokens = np.array(tokens)
