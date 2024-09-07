import numpy as np

lexema = ''
with open('exemplo01.txt', 'r') as arquivo:
    palavra = arquivo.read()

tokens = []
lexemas = []

espacos = [' ', '\n', '\t', '\r']
parentizacao = ['{', '}', '(', ')', '[', ']']

literalLimiter = False;
charLimiter = False;
strLimiter = False;

for i in range(len(palavra)):
    if palavra[i] == '_':
        if literalLimiter:
            lexema = lexema + palavra[i]
            tokens.append(13)
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
            lexema = lexema + palavra[i]
            tokens.append(38)
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
                print('Erro: Char não pode ter mais de um caractere')
                break
            else:
                lexema = lexema + palavra[i]
                tokens.append(39)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                print(lexema)
                lexema = ''
        else:
            lexema = lexema + palavra[i]
            charLimiter = True
    elif (palavra[i] not in espacos) or literalLimiter or charLimiter or strLimiter:
        lexema = lexema + palavra[i]
        
    else:
        lexema = ''
        
    print(lexema)
    
    if lexema == 'write':
        tokens.append(0)
        lexemas.append(lexema)
        
    elif lexema == 'while':
        tokens.append(1)
        lexemas.append(lexema)
        
    elif lexema == 'until':
        tokens.append(2)
        lexemas.append(lexema)
        
    elif lexema == 'to':
        tokens.append(3)
        lexemas.append(lexema)
        
    elif lexema == 'then':
        tokens.append(4)    
        lexemas.append(lexema)
        
    elif lexema == 'string':
        tokens.append(5)
        lexemas.append(lexema)
        
    elif lexema == 'repeat':
        tokens.append(6)
        lexemas.append(lexema)
        
    elif lexema == 'real':
        tokens.append(7)
        lexemas.append(lexema)
        
    elif lexema == 'read':
        tokens.append(8)
        lexemas.append(lexema)
        
    elif lexema == 'program':
        tokens.append(9)
        lexemas.append(lexema)
        
    elif lexema == 'procedure':
        tokens.append(10)
        lexemas.append(lexema)
        
    elif lexema == 'or':
        tokens.append(11)
        lexemas.append(lexema)
        
    elif lexema == 'of':
        tokens.append(12)
        lexemas.append(lexema)
        
    elif lexema == 'integer':
        tokens.append(14)
        lexemas.append(lexema)
        
    elif lexema == 'if':
        tokens.append(15)
        lexemas.append(lexema)
        
    elif lexema == 'for':
        tokens.append(18)
        lexemas.append(lexema)
        
    elif lexema == 'end':
        tokens.append(19)
        lexemas.append(lexema)
        
    elif lexema == 'else':
        tokens.append(20)
        lexemas.append(lexema)
        
    elif lexema == 'do':
        tokens.append(21)
        lexemas.append(lexema)
        
    elif lexema == 'declaravariaveis':
        tokens.append(22)
        lexemas.append(lexema)
        
    elif lexema == 'const':
        tokens.append(23)
        lexemas.append(lexema)
        
    elif lexema == 'char':
        tokens.append(24)
        lexemas.append(lexema)
        
    elif lexema == 'chamaprocedure':
        tokens.append(25)
        lexemas.append(lexema)
        
    elif lexema == 'begin':
        tokens.append(26)
        lexemas.append(lexema)
        
    elif lexema == 'array':
        tokens.append(27)
        lexemas.append(lexema)
        
    elif lexema == 'and':
        tokens.append(28)
        lexemas.append(lexema)
        
    elif lexema == '>=':
        tokens.append(29)
        lexemas.append(lexema)
        
    elif lexema == '>':
        tokens.append(30)
        lexemas.append(lexema)
        
    elif lexema == '=':
        tokens.append(31)
        lexemas.append(lexema)
        
    elif lexema == '<>':
        tokens.append(32)
        lexemas.append(lexema)
        
    elif lexema == '<=':
        tokens.append(33)
        lexemas.append(lexema)
        
    elif lexema == '<':
        tokens.append(34)
        lexemas.append(lexema)
        
    elif lexema == '+':
        tokens.append(35)
        lexemas.append(lexema)
        
    elif lexema == ']':
        tokens.append(40)
        lexemas.append(lexema)
        
    elif lexema == '[':
        tokens.append(41)
        lexemas.append(lexema)
        
    elif lexema == ';':
        tokens.append(42)
        lexemas.append(lexema)
        
    elif lexema == ':':
        tokens.append(43)
        lexemas.append(lexema)
        
    elif lexema == '/':
        tokens.append(44)
        lexemas.append(lexema)
        
    elif lexema == '..':
        tokens.append(45)
        lexemas.append(lexema)
        
    elif lexema == '.':
        tokens.append(46)
        lexemas.append(lexema)
        
    elif lexema == ',':
        tokens.append(47)
        lexemas.append(lexema)
        
    elif lexema == '*':
        tokens.append(48)
        lexemas.append(lexema)
        
    elif lexema == ')':
        tokens.append(49)
        lexemas.append(lexema)
        
    elif lexema == '(':
        tokens.append(50)
        lexemas.append(lexema)
        
    elif lexema == '$':
        tokens.append(51)
        lexemas.append(lexema)
        
    elif lexema == '-':
        tokens.append(52)
        lexemas.append(lexema)
        
    # confirmar
        
    elif lexema == 'identificador':
        tokens.append(16)
        lexemas.append(lexema)
        
    elif lexema == 'î':
        tokens.append(17)
        lexemas.append(lexema)
        
    elif lexema == 'numreal':
        tokens.append(36)
        lexemas.append(lexema)
        
    elif lexema == 'numinteiro':
        tokens.append(37)
        lexemas.append(lexema)
        
    elif lexema == 'numreal':
        tokens.append(36)
        lexemas.append(lexema)
        
    elif lexema == 'numinteiro':
        tokens.append(37)
        lexemas.append(lexema)
        
for i in range(0,len(tokens)):
    print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: 1' )

tokens = np.array(tokens)

