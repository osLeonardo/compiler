import numpy as np

def getProducoes():
    producoes = [[9, 16, 42, 54, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1]]                                   # P0:  <PROGRAMA>       ::= "program" "identificador" ";" <BLOCO> "."
    producoes = np.append(producoes, [[55, 56, 57, 58, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P1:  <BLOCO>          ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    producoes = np.append(producoes, [[23, 16, 31, 59, 42, 60, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P2:  <DCLCONST>       ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P3:  <DCLCONST>       ::= î
    producoes = np.append(producoes, [[16, 31, 59, 42, 60, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P4:  <LDCONST>        ::= "identificador" "=" <TIPO> ";" <LDCONST>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P5:  <LDCONST>        ::= î
    producoes = np.append(producoes, [[22, 61, 43, 59, 42, 62, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P6:  <DCLVAR>         ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P7:  <DCLVAR>         ::= î
    producoes = np.append(producoes, [[16, 63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P8:  <LID>            ::= "identificador" <REPIDENT>
    producoes = np.append(producoes, [[47, 16, 63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P9:  <REPIDENT>       ::= "," "identificador" <REPIDENT>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P10: <REPIDENT>       ::= î
    producoes = np.append(producoes, [[61, 43, 59, 42, 62, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P11: <LDVAR>          ::= <LID> ":" <TIPO> ";" <LDVAR>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P12: <LDVAR>          ::= î
    producoes = np.append(producoes, [[27, 41, 37, 45, 37, 40, 12, 64, -1, -1, -1, -1, -1, -1]], axis=0)    # P13: <TIPO>           ::= "array" "[" "numinteiro" ".." "numinteiro" "]" "of" <TIPOARRAY>
    producoes = np.append(producoes, [[14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P14: <TIPOARRAY>      ::= "integer"
    producoes = np.append(producoes, [[24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P15: <TIPOARRAY>      ::= "char"
    producoes = np.append(producoes, [[5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P16: <TIPOARRAY>      ::= "string"
    producoes = np.append(producoes, [[7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P17: <TIPOARRAY>      ::= "real"
    producoes = np.append(producoes, [[14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P18: <TIPO>           ::= "integer"
    producoes = np.append(producoes, [[24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P19: <TIPO>           ::= "char"
    producoes = np.append(producoes, [[5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P20: <TIPO>           ::= "string"
    producoes = np.append(producoes, [[7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P21: <TIPO>           ::= "real"
    producoes = np.append(producoes, [[10, 16, 65, 57, 58, 42, 55, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P22: <DCLPROC>        ::= "procedure" "identificador" <DEFPAR> <DCLVAR> <CORPO> ";" <DCLPROC>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P23: <DCLPROC>        ::= î
    producoes = np.append(producoes, [[50, 61, 43, 59, 42, 62, 49, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P24: <DEFPAR>         ::= "(" <LID> ":" <TIPO> ";" <LDVAR> ")"
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P25: <DEFPAR>         ::= î
    producoes = np.append(producoes, [[26, 66, 42, 67, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P26: <CORPO>          ::= "begin" <COMANDO> ";" <REPCOMANDO> "end"
    producoes = np.append(producoes, [[66, 42, 67, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P27: <REPCOMANDO>     ::= <COMANDO> ";" <REPCOMANDO>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P28: <REPCOMANDO>     ::= î
    producoes = np.append(producoes, [[15, 41, 68, 40, 4, 26, 66, 19, 69, -1, -1, -1, -1, -1]], axis=0)     # P29: <COMANDO>        ::= "if" "[" <EXPRESSAO> "]" "then" "begin" <COMANDO> "end" <ELSEPARTE>
    producoes = np.append(producoes, [[1, 41, 68, 40, 21, 26, 66, 19, -1, -1, -1, -1, -1, -1]], axis=0)     # P30: <COMANDO>        ::= "while" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    producoes = np.append(producoes, [[6, 66, 2, 41, 68, 40, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)      # P31: <COMANDO>        ::= "repeat" <COMANDO> "until" "[" <EXPRESSAO> "]"
    producoes = np.append(producoes, [[8, 50, 70, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P32: <COMANDO>        ::= "read" "(" <VARIAVEL> ")"
    producoes = np.append(producoes, [[25, 16, 72, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P33: <COMANDO>        ::= "chamaprocedure" "identificador" <PARAMETROS>
    producoes = np.append(producoes, [[0, 50, 73, 74, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     # P34: <COMANDO>        ::= "write" "(" <ITEMSAIDA> <REPITEM> ")"
    producoes = np.append(producoes, [[18, 41, 16, 31, 68, 40, 3, 41, 68, 40, 21, 26, 66, 19]], axis=0)     # P35: <COMANDO>        ::= "for" "[" "identificador" "=" <EXPRESSAO> "]" "to" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P36: <COMANDO>        ::= î
    producoes = np.append(producoes, [[50, 61, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P37: <PARAMETROS>     ::= "(" <LID> ")"
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P38: <PARAMETROS>     ::= î
    producoes = np.append(producoes, [[13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P39: <ITEMSAIDA>      ::= "literal"
    producoes = np.append(producoes, [[68, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P40: <ITEMSAIDA>      ::= <EXPRESSAO>
    producoes = np.append(producoes, [[47, 73, 74, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P41: <REPITEM>        ::= "," <ITEMSAIDA> <REPITEM>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P42: <REPITEM>        ::= î
    producoes = np.append(producoes, [[75, 76, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P43: <EXPRESSAO>      ::= <TERMO> <REPEXP> <REPEXPSIMP>
    producoes = np.append(producoes, [[78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P44: <TERMO>          ::= <FATOR> <REPTERMO>
    producoes = np.append(producoes, [[37, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P45: <FATOR>          ::= "numinteiro"
    producoes = np.append(producoes, [[16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P46: <FATOR>          ::= "identificador"
    producoes = np.append(producoes, [[38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P47: <FATOR>          ::= "nomestring"
    producoes = np.append(producoes, [[39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P48: <FATOR>          ::= "nomechar"
    producoes = np.append(producoes, [[36, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P49: <FATOR>          ::= "numreal"
    producoes = np.append(producoes, [[50, 68, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P50: <FATOR>          ::= "(" <EXPRESSAO> ")"
    producoes = np.append(producoes, [[31, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P51: <REPEXPSIMP>     ::= "=" <EXPSIMP>
    producoes = np.append(producoes, [[34, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P52: <REPEXPSIMP>     ::= "<" <EXPSIMP>
    producoes = np.append(producoes, [[30, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P53: <REPEXPSIMP>     ::= ">" <EXPSIMP>
    producoes = np.append(producoes, [[29, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P54: <REPEXPSIMP>     ::= ">=" <EXPSIMP>
    producoes = np.append(producoes, [[33, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P55: <REPEXPSIMP>     ::= "<=" <EXPSIMP>
    producoes = np.append(producoes, [[32, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P56: <REPEXPSIMP>     ::= "<>" <EXPSIMP>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P57: <REPEXPSIMP>     ::= î
    producoes = np.append(producoes, [[35, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P58: <EXPSIMP>        ::= "+" <TERMO> <REPEXP>
    producoes = np.append(producoes, [[52, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P59: <EXPSIMP>        ::= "-" <TERMO> <REPEXP>
    producoes = np.append(producoes, [[75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P60: <EXPSIMP>        ::= <TERMO> <REPEXP>
    producoes = np.append(producoes, [[35, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P61: <REPEXP>         ::= "+" <TERMO> <REPEXP>
    producoes = np.append(producoes, [[52, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P62: <REPEXP>         ::= "-" <TERMO> <REPEXP>
    producoes = np.append(producoes, [[11, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P63: <REPEXP>         ::= "or" <TERMO> <REPEXP>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P64: <REPEXP>         ::= î
    producoes = np.append(producoes, [[48, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P65: <REPTERMO>       ::= "*" <FATOR> <REPTERMO>
    producoes = np.append(producoes, [[44, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P66: <REPTERMO>       ::= "/" <FATOR> <REPTERMO>
    producoes = np.append(producoes, [[28, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P67: <REPTERMO>       ::= "and" <FATOR> <REPTERMO>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P68: <REPTERMO>       ::= î
    producoes = np.append(producoes, [[20, 26, 66, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P69: <ELSEPARTE>      ::= "else" "begin" <COMANDO> "end"
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P70: <ELSEPARTE>      ::= î
    producoes = np.append(producoes, [[16, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P71: <VARIAVEL>       ::= "identificador" <REPVARIAVEL>
    producoes = np.append(producoes, [[47, 16, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P72: <REPVARIAVEL>    ::= "," "identificador" <REPVARIAVEL>
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    # P73: <REPVARIAVEL>    ::= î
    
    return producoes

def getTabParsing():
    tabParsing = np.zeros((82, 82), dtype=int)
    
    tabParsing[53][9] = 1    # <PROGRAMA> ::= "program" "identificador" ";" <BLOCO> "."
    
    tabParsing[54][10] = 2   # <BLOCO> ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    tabParsing[54][23] = 2   # <BLOCO> ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    tabParsing[54][22] = 2   # <BLOCO> ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    tabParsing[54][26] = 2   # <BLOCO> ::= <DCLPROC> <DCLCONST> <DCLVAR> <CORPO>
    
    tabParsing[56][23] = 3   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    
    tabParsing[57][22] = 7   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    
    tabParsing[58][26] = 27  # <CORPO> ::= "begin" <COMANDO> ";" <REPCOMANDO> "end"
    
    tabParsing[60][16] = 5   # <LDCONST> ::= "identificador" "=" <TIPO> ";" <LDCONST>
    
    tabParsing[61][16] = 9   # <LID> ::= "identificador" <REPIDENT>
    
    tabParsing[63][43] = 11  # <REPIDENT> ::= "," "identificador" <REPIDENT>
    tabParsing[63][49] = 11  # <REPIDENT> ::= "," "identificador" <REPIDENT>
    tabParsing[63][47] = 9   # <LID> ::= "identificador" <REPIDENT>
    
    tabParsing[62][16] = 12  # <LDVAR> ::= <LID> ":" <TIPO> ";" <LDVAR>
    
    tabParsing[59][27] = 14  # <TIPO> ::= "array" "[" "numinteiro" ".." "numinteiro" "]" "of" <TIPOARRAY>
    
    tabParsing[64][14] = 15  # <TIPOARRAY> ::= "integer"
    tabParsing[64][24] = 16  # <TIPOARRAY> ::= "char"
    tabParsing[64][5] = 17   # <TIPOARRAY> ::= "string"
    tabParsing[64][7] = 18   # <TIPOARRAY> ::= "real"
    
    tabParsing[59][14] = 19  # <TIPO> ::= "integer"
    tabParsing[59][24] = 20  # <TIPO> ::= "char"
    tabParsing[59][5] = 21   # <TIPO> ::= "string"
    tabParsing[59][7] = 22   # <TIPO> ::= "real"
    
    tabParsing[55][10] = 23  # <DCLPROC> ::= "procedure" "identificador" <DEFPAR> <DCLVAR> <CORPO> ";" <DCLPROC>
    tabParsing[55][23] = 3   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[55][22] = 7   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[55][26] = 27  # <CORPO> ::= "begin" <COMANDO> ";" <REPCOMANDO> "end"
    
    tabParsing[65][50] = 25  # <DEFPAR> ::= "(" <LID> ":" <TIPO> ";" <LDVAR> ")"
   
    tabParsing[67][15] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][1] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][6] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][8] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][25] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][0] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][18] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][42] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    
    tabParsing[66][15] = 30  # <COMANDO> ::= "if" "[" <EXPRESSAO> "]" "then" "begin" <COMANDO> "end" <ELSEPARTE>
    tabParsing[66][1] = 31   # <COMANDO> ::= "while" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    tabParsing[66][6] = 32   # <COMANDO> ::= "repeat" <COMANDO> "until" "[" <EXPRESSAO> "]"
    tabParsing[66][8] = 33   # <COMANDO> ::= "read" "(" <VARIAVEL> ")"
    tabParsing[66][25] = 34  # <COMANDO> ::= "chamaprocedure" "identificador" <PARAMETROS>
    tabParsing[66][0] = 35   # <COMANDO> ::= "write" "(" <ITEMSAIDA> <REPITEM> ")"
    tabParsing[66][18] = 36  # <COMANDO> ::= "for" "[" "identificador" "=" <EXPRESSAO> "]" "to" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    tabParsing[66][17] = 37  # <COMANDO> ::= î
    
    tabParsing[72][50] = 38  # <PARAMETROS> ::= "(" <LID> ")"
    
    tabParsing[73][13] = 40  # <ITEMSAIDA> ::= "literal"
    tabParsing[73][37] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][16] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][38] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][39] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][36] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][50] = 40  # <ITEMSAIDA> ::= <EXPRESSAO>
    
    tabParsing[74][47] = 43  # <REPITEM> ::= "," <ITEMSAIDA> <REPITEM>
    
    tabParsing[68][37] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][16] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][38] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][39] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][36] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][50] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>

    tabParsing[75][37] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][16] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][38] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][39] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][36] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][50] = 45  # <TERMO> ::= <FATOR> <REPTERMO>

    tabParsing[78][37] = 46  # <FATOR> ::= "numinteiro"
    tabParsing[78][16] = 47  # <FATOR> ::= "identificador"
    tabParsing[78][38] = 48  # <FATOR> ::= "nomestring"
    tabParsing[78][39] = 49  # <FATOR> ::= "nomechar"
    tabParsing[78][36] = 50  # <FATOR> ::= "numreal"
    tabParsing[78][50] = 51  # <FATOR> ::= "(" <EXPRESSAO> ")"
    
    tabParsing[77][31] = 52  # <REPEXPSIMP> ::= "=" <EXPSIMP>
    tabParsing[77][34] = 53  # <REPEXPSIMP> ::= "<" <EXPSIMP>
    tabParsing[77][30] = 54  # <REPEXPSIMP> ::= ">" <EXPSIMP>
    tabParsing[77][29] = 55  # <REPEXPSIMP> ::= ">=" <EXPSIMP>
    tabParsing[77][33] = 56  # <REPEXPSIMP> ::= "<=" <EXPSIMP>
    tabParsing[77][32] = 57  # <REPEXPSIMP> ::= "<>" <EXPSIMP>
    
    tabParsing[76][35] = 59  # <EXPSIMP> ::= "+" <TERMO> <REPEXP>
    tabParsing[76][52] = 60  # <EXPSIMP> ::= "-" <TERMO> <REPEXP>
    tabParsing[76][37] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>
    tabParsing[76][16] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>
    tabParsing[76][38] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>
    tabParsing[76][39] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>
    tabParsing[76][36] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>
    tabParsing[76][50] = 61  # <EXPSIMP> ::= <TERMO> <REPEXP>

    tabParsing[76][35] = 62  # <REPEXP> ::= "+" <TERMO> <REPEXP>
    tabParsing[76][52] = 63  # <REPEXP> ::= "-" <TERMO> <REPEXP>
    tabParsing[76][11] = 64  # <REPEXP> ::= "or" <TERMO> <REPEXP>
    
    tabParsing[79][48] = 66  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][44] = 67  # <REPTERMO> ::= "/" <FATOR> <REPTERMO>
    tabParsing[79][28] = 68  # <REPTERMO> ::= "and" <FATOR> <REPTERMO>
    
    tabParsing[69][20] = 70  # <ELSEPARTE> ::= "else" "begin" <COMANDO> "end"
    
    tabParsing[70][16] = 72  # <VARIAVEL> ::= "identificador" <REPVARIAVEL>
    
    tabParsing[71][47] = 73  # <REPVARIAVEL> ::= "," "identificador" <REPVARIAVEL>

    return tabParsing

def sintatico(token_array):
    # Variável para armazenar o array de tokens (que irá alimentar o sintático)
    tokens = np.array(token_array)

    # Obter produções e tabela de parsing
    producoes = getProducoes()
    tabParsing = getTabParsing()

    pilha = [51]  # $
    pilha = np.hstack([producoes[0][:], pilha])  # Empilhar a primeira produção (P0: <PROGRAMA>)

    print("Tokens iniciais:", tokens)
    print("Pilha inicial:", pilha)

    X = pilha[0]
    a = tokens[0]

    while X != 51:  # $
        print("Pilha:", pilha)  # Obrigatório mostrar a pilha a cada iteração
        print("X:", X)
        print("a:", a)
        if X == 17:  # Vazio
            pilha = np.delete(pilha, [0])
            X = pilha[0]
        else:
            if X <= 52:  # X é terminal
                if X == a:
                    pilha = np.delete(pilha, [0])
                    tokens = np.delete(tokens, [0])
                    if tokens.size != 0:
                        a = tokens[0]
                    else:
                        a = 51  # Fim da entrada
                    if pilha.size != 0:
                        X = pilha[0]
                    else:
                        X = 51  # Fim da pilha
                else:
                    print('Error: Unexpected token', a)
                    break
            else:  # X é não terminal
                if tabParsing[X][a] != 0:
                    producao = producoes[tabParsing[X][a] - 1]
                    pilha = np.delete(pilha, [0])
                    pilha = np.hstack([producao[producao != -1], pilha])
                    X = pilha[0]
                else:
                    print('Error: No production found for', X, 'and', a)
                    break

    if X == 51 and a == 51:
        print("Parsing completed successfully.")
    else:
        print("Parsing failed.")