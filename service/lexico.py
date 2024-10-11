import numpy as np
import os

def lexico():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/content/01.txt')

    with open(file_path, 'r') as arquivo:
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
    catchError = ''
    currentLine = 1
    lineComment = False
    blockComment = False
    literalLimiter = False
    charLimiter = False
    strLimiter = False
    numLimiter = False

    for i in range(len(palavra)):
        if lineComment or blockComment:
            if lineComment and palavra[i] == '\n':
                lineComment = False
                currentLine += 1
            elif blockComment and palavra[i:i+2] == '*/':
                blockComment = False
                i += 1
            continue

        if palavra[i:i+2] == '//':
            lineComment = True
            i += 1

        elif palavra[i:i+2] == '/*':
            blockComment = True
            i += 1

        elif palavra[i] == '\n':
            currentLine += 1
            lineComment = False

        elif palavra[i] == '_':
            if literalLimiter:
                tokens.append(13)
                lines.append(currentLine)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                lexema = ''
            else: 
                literalLimiter = True

        elif palavra[i] == '"':
            if strLimiter:
                if len(lexema) > 21:
                    catchError = f'Erro: String não pode ter mais de 20 caracteres. Linha: {currentLine}'
                    break
                tokens.append(38)
                lines.append(currentLine)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                lexema = ''
            else:
                strLimiter = True

        elif palavra[i] == "'":
            if charLimiter:
                if len(lexema) > 2:
                    catchError = f'Erro: Char não pode ter mais de um caractere. Linha: {currentLine}'
                    break
                else:
                    tokens.append(39)
                    lines.append(currentLine)
                    lexemas.append(lexema)
                    strLimiter = False
                    charLimiter = False
                    literalLimiter = False
                    lexema = ''
            else:
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
                            catchError = f'Erro: Número real não pode conter mais de 5 dígitos antes do divisor. Linha: {currentLine}'
                            break
                        elif len(parts[1]) > 2:
                            catchError = f'Erro: Número real não pode conter mais de 2 dígitos após do divisor. Linha: {currentLine}'
                            break
                        else:
                            tokens.append(36)
                            lines.append(currentLine)
                    else:
                        if len(lexema) > 5:
                            catchError = f'Erro: Número inteiro não pode conter mais de 5 dígitos. Linha: {currentLine}'
                            break
                        else:
                            tokens.append(37)
                            lines.append(currentLine)
                    lexemas.append(lexema)
                    lexema = ''
                    numLimiter = False
            else:
                lexema = lexema + palavra[i]
                numLimiter = True

        elif palavra[i].isalpha():
            lexema = lexema + palavra[i]
            if charLimiter or strLimiter or literalLimiter:
                continue
            elif lexema in reservados and (palavra[i+1] in espacos or palavra[i+1] in simbolos):
                tokens.append(reservados.index(lexema))
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

            elif len(lexema) > 20:
                catchError = f'Erro: Identificador não pode ter mais de 20 caracteres. Linha: {currentLine}'
                break

            elif palavra[i+1] in espacos or palavra[i+1] in simbolos:
                tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

        elif palavra[i] in simbolos:

            if lexema:
                if charLimiter or strLimiter or literalLimiter:
                    lexema = lexema + palavra[i]
                    continue
                elif lexema in reservados:
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
                if charLimiter or strLimiter or literalLimiter:
                    lexema = lexema + palavra[i]
                    continue
                elif lexema in reservados:
                    tokens.append(reservados.index(lexema))
                else:
                    tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

    for i in range(0,len(tokens)):
        print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: ' +str(lines[i]))

    if (catchError != ''):
        print(catchError)

    tokens = np.array(tokens)