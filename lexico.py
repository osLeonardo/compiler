import numpy as np

with open('exemplo01.txt', 'r') as arquivo:
    palavra = arquivo.read()

tokens = []
lexemas = []
lines = []
espacos = [' ', '\n', '\t', '\r']
simbolos = ['{', '}', '(', ')', '[', ']', '-', '+', '*', '/', '=', '<', '>', '.', ',', ';', ':']
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
        lineComment = False;

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
        
        if lexema in reservados and palavra[i+1] in espacos:
            continue
            
        elif len(lexema) > 10:
            print(f'Erro: Identificador não pode ter mais de 10 caracteres. Linha: {currentLine}')
            break
        
        elif palavra[i+1] in espacos:
            tokens.append(16)
            lines.append(currentLine)
            lexemas.append(lexema)
            print(lexema)
            lexema = ''
    
    elif (palavra[i] not in espacos) or literalLimiter or charLimiter or strLimiter:
        lexema = lexema + palavra[i]
    
    else:
        lexema = ''
    
    print(lexema)
    
    if lexema == 'write':
        tokens.append(0)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'while':
        tokens.append(1)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'until':
        tokens.append(2)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'to':
        tokens.append(3)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'then':
        tokens.append(4) 
        lines.append(currentLine)   
        lexemas.append(lexema)
    
    elif lexema == 'string':
        tokens.append(5)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'repeat':
        tokens.append(6)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'real':
        tokens.append(7)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'read':
        tokens.append(8)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'program':
        tokens.append(9)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'procedure':
        tokens.append(10)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'or':
        tokens.append(11)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'of':
        tokens.append(12)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'integer':
        tokens.append(14)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'if':
        tokens.append(15)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'for':
        tokens.append(18)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'end':
        tokens.append(19)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'else':
        tokens.append(20)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'do':
        tokens.append(21)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'declaravariaveis':
        tokens.append(22)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'const':
        tokens.append(23)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'char':
        tokens.append(24)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'chamaprocedure':
        tokens.append(25)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'begin':
        tokens.append(26)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'array':
        tokens.append(27)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == 'and':
        tokens.append(28)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    # TODO: checkar simbolos na parte superior do código similar as aspas
    
    elif lexema == '>=':
        tokens.append(29)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '>':
        tokens.append(30)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '=':
        tokens.append(31)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '<>':
        tokens.append(32)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '<=':
        tokens.append(33)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '<':
        tokens.append(34)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '+':
        tokens.append(35)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == ']':
        tokens.append(40)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '[':
        tokens.append(41)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == ';':
        tokens.append(42)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == ':':
        tokens.append(43)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '/':
        tokens.append(44)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '..':
        tokens.append(45)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '.':
        tokens.append(46)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == ',':
        tokens.append(47)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '*':
        tokens.append(48)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == ')':
        tokens.append(49)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '(':
        tokens.append(50)
        lines.append(currentLine)
        lexemas.append(lexema)
    
    elif lexema == '-':
        tokens.append(52)
        lines.append(currentLine)
        lexemas.append(lexema)

for i in range(0,len(tokens)):
    print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: ' +str(lines[i]))

tokens = np.array(tokens)
