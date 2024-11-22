from service import simbolos
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
    
    tabParsing[55][10] = 23  # <DCLPROC> ::= "procedure" "identificador" <DEFPAR> <DCLVAR> <CORPO> ";" <DCLPROC>
    tabParsing[55][23] = 3   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[55][22] = 7   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[55][26] = 27  # <CORPO> ::= "begin" <COMANDO> ";" <REPCOMANDO> "end"
    
    tabParsing[56][23] = 3   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[56][22] = 4   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[56][26] = 4   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[56][42] = 4   # <DCLCONST> ::= "const" "identificador" "=" <TIPO> ";" <LDCONST>
    
    tabParsing[57][22] = 7   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[57][26] = 8   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[57][42] = 8   # <DCLVAR> ::= "declaravariaveis" <LID> ":" <TIPO> ";" <LDVAR>
    
    tabParsing[58][26] = 27  # <CORPO> ::= "begin" <COMANDO> ";" <REPCOMANDO> "end"
    
    tabParsing[59][14] = 19  # <TIPO> ::= "integer"
    tabParsing[59][24] = 20  # <TIPO> ::= "char"
    tabParsing[59][5] = 21   # <TIPO> ::= "string"
    tabParsing[59][7] = 22   # <TIPO> ::= "real"
    tabParsing[59][27] = 14  # <TIPO> ::= "array" "[" "numinteiro" ".." "numinteiro" "]" "of" <TIPOARRAY>
    
    tabParsing[60][16] = 5   # <LDCONST> ::= "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[60][22] = 6   # <LDCONST> ::= "identificador" "=" <TIPO> ";" <LDCONST>
    tabParsing[60][26] = 6   # <LDCONST> ::= "identificador" "=" <TIPO> ";" <LDCONST>
    
    tabParsing[61][16] = 9   # <LID> ::= "identificador" <REPIDENT>
    
    tabParsing[62][16] = 12  # <LDVAR> ::= <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[62][26] = 13  # <LDVAR> ::= <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[62][42] = 13  # <LDVAR> ::= <LID> ":" <TIPO> ";" <LDVAR>
    tabParsing[62][49] = 13  # <LDVAR> ::= <LID> ":" <TIPO> ";" <LDVAR>
    
    tabParsing[63][43] = 11  # <REPIDENT> ::= "," "identificador" <REPIDENT>
    tabParsing[63][49] = 11  # <REPIDENT> ::= "," "identificador" <REPIDENT>
    tabParsing[63][47] = 10   # <LID> ::= "identificador" <REPIDENT>
    
    tabParsing[64][14] = 15  # <TIPOARRAY> ::= "integer"
    tabParsing[64][24] = 16  # <TIPOARRAY> ::= "char"
    tabParsing[64][5] = 17   # <TIPOARRAY> ::= "string"
    tabParsing[64][7] = 18   # <TIPOARRAY> ::= "real"
    
    tabParsing[65][50] = 25  # <DEFPAR> ::= "(" <LID> ":" <TIPO> ";" <LDVAR> ")"
    tabParsing[65][22] = 26  # <DEFPAR> ::= "(" <LID> ":" <TIPO> ";" <LDVAR> ")"
    tabParsing[65][26] = 26  # <DEFPAR> ::= "(" <LID> ":" <TIPO> ";" <LDVAR> ")"
    
    tabParsing[66][15] = 30  # <COMANDO> ::= "if" "[" <EXPRESSAO> "]" "then" "begin" <COMANDO> "end" <ELSEPARTE>
    tabParsing[66][1] = 31   # <COMANDO> ::= "while" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    tabParsing[66][6] = 32   # <COMANDO> ::= "repeat" <COMANDO> "until" "[" <EXPRESSAO> "]"
    tabParsing[66][8] = 33   # <COMANDO> ::= "read" "(" <VARIAVEL> ")"
    tabParsing[66][25] = 34  # <COMANDO> ::= "chamaprocedure" "identificador" <PARAMETROS>
    tabParsing[66][0] = 35   # <COMANDO> ::= "write" "(" <ITEMSAIDA> <REPITEM> ")"
    tabParsing[66][18] = 36  # <COMANDO> ::= "for" "[" "identificador" "=" <EXPRESSAO> "]" "to" "[" <EXPRESSAO> "]" "do" "begin" <COMANDO> "end"
    tabParsing[66][2] = 37  # <COMANDO> ::= î
    tabParsing[66][19] = 37  # <COMANDO> ::= î
    tabParsing[66][42] = 37  # <COMANDO> ::= î

    tabParsing[67][15] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][1] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][6] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][8] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][25] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][0] = 28   # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][18] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][42] = 28  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    tabParsing[67][19] = 29  # <REPCOMANDO> ::= <COMANDO> ";" <REPCOMANDO>
    
    tabParsing[68][16] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][36] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][37] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>    
    tabParsing[68][38] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][39] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    tabParsing[68][50] = 44  # <EXPRESSAO> ::= <TERMO> <REPEXP> <REPEXPSIMP>
    
    tabParsing[69][20] = 70  # <ELSEPARTE> ::= "else" "begin" <COMANDO> "end"
    tabParsing[69][42] = 70  # <ELSEPARTE> ::= "else" "begin" <COMANDO> "end"
    
    tabParsing[70][16] = 72  # <VARIAVEL> ::= "identificador" <REPVARIAVEL>
    
    tabParsing[71][47] = 73  # <REPVARIAVEL> ::= "," "identificador" <REPVARIAVEL>
    tabParsing[71][49] = 74  # <REPVARIAVEL> ::= "," "identificador" <REPVARIAVEL>
    
    tabParsing[72][50] = 38  # <PARAMETROS> ::= "(" <LID> ")"
    tabParsing[72][42] = 39  # <PARAMETROS> ::= "(" <LID> ")"
    
    tabParsing[73][13] = 40  # <ITEMSAIDA> ::= "literal"
    tabParsing[73][11] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][28] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][29] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][30] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][31] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][32] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][33] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][34] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][35] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][35] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][36] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][37] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][38] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][39] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][44] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][48] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][16] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][50] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    tabParsing[73][52] = 41  # <ITEMSAIDA> ::= <EXPRESSAO>
    
    tabParsing[74][47] = 42  # <REPITEM> ::= "," <ITEMSAIDA> <REPITEM>
    tabParsing[74][49] = 43  # <REPITEM> ::= "," <ITEMSAIDA> <REPITEM>

    tabParsing[75][16] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][36] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][37] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][38] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
    tabParsing[75][39] = 45  # <TERMO> ::= <FATOR> <REPTERMO>
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
    tabParsing[77][4] = 58  # Estado <REPEXPSIMP>, token "then" -> Produção 57
    tabParsing[77][21] = 58  # Estado <REPEXPSIMP>, token "do" -> Produção 57
    tabParsing[77][2] = 58  # Estado <REPEXPSIMP>, token "until" -> Produção 57
    tabParsing[77][3] = 58  # Estado <REPEXPSIMP>, token "to" -> Produção 57
    tabParsing[77][47] = 58  # Estado <REPEXPSIMP>, token "," -> Produção 57
    tabParsing[77][49] = 58  # Estado <REPEXPSIMP>, token ")" -> Produção 57
    tabParsing[77][40] = 58  # Estado <REPEXPSIMP>, token "]" -> Produção 57
    tabParsing[77][41] = 58  # Estado <REPEXPSIMP>, token "[" -> Produção 57
    
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
    tabParsing[76][4] = 65  # Estado <REPEXP>, token "then" -> Produção 64
    tabParsing[76][21] = 65  # Estado <REPEXP>, token "do" -> Produção 64
    tabParsing[76][2] = 65  # Estado <REPEXP>, token "until" -> Produção 64
    tabParsing[76][3] = 65  # Estado <REPEXP>, token "to" -> Produção 64
    tabParsing[76][47] = 65  # Estado <REPEXP>, token "," -> Produção 64
    tabParsing[76][49] = 65  # Estado <REPEXP>, token ")" -> Produção 64
    tabParsing[76][40] = 65  # Estado <REPEXP>, token "]" -> Produção 64
    tabParsing[76][41] = 65  # Estado <REPEXP>, token "[" -> Produção 64
    tabParsing[76][29] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][30] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][31] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][32] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][33] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][34] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[76][35] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>

    tabParsing[79][48] = 66  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][44] = 67  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][28] = 68  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][16] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][29] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][30] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][31] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][32] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][33] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][34] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][35] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][36] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][37] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][38] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][39] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][50] = 69  # <REPTERMO> ::= "*" <FATOR> <REPTERMO>
    tabParsing[79][4] = 69  # <REPTERMO>, token "then" -> Produção 68
    tabParsing[79][21] = 69  # <REPTERMO>, token "do" -> Produção 68
    tabParsing[79][2] = 69  # <REPTERMO>, token "until" -> Produção 68
    tabParsing[79][3] = 69  # <REPTERMO>, token "to" -> Produção 68
    tabParsing[79][47] = 69  # <REPTERMO>, token "," -> Produção 68
    tabParsing[79][49] = 69  # <REPTERMO>, token ")" -> Produção 68
    tabParsing[79][40] = 69  # <REPTERMO>, token "]" -> Produção 68
    tabParsing[79][41] = 69  # <REPTERMO>, token "[" -> Produção 68
    
    tabParsing[80][35] = 59  # Estado <EXPSIMP>, token "+" -> Produção 58
    tabParsing[80][52] = 60  # Estado <EXPSIMP>, token "-" -> Produção 59
    tabParsing[80][16] = 61  # Estado <EXPSIMP>, token "identificador" -> Produção 60
    tabParsing[80][37] = 61  # Estado <EXPSIMP>, token "numinteiro" -> Produção 60
    tabParsing[80][36] = 61  # Estado <EXPSIMP>, token "numreal" -> Produção 60
    tabParsing[80][38] = 61  # Estado <EXPSIMP>, token "nomestring" -> Produção 60
    tabParsing[80][39] = 61  # Estado <EXPSIMP>, token "nomechar" -> Produção 60
    tabParsing[80][50] = 61  # Estado <EXPSIMP>, token "(" -> Produção 60

    return tabParsing

def check_variable_declared(tabela_simbolos, var_name):
    result = tabela_simbolos.lookup(var_name)
    if isinstance(result, str):
        return result
    return "OK"

def check_data_types(var1, var2, operation):
    if operation == "+":
        if isinstance(var1, (int, float)) and isinstance(var2, (int, float)):
            return "OK"
        elif isinstance(var1, str) and isinstance(var2, str):
            return "OK"
        else:
            return "Tipos incompatíveis para soma."
    return "OK"

def check_division_by_zero(divisor):
    if divisor == 0:
        return "Divisão por zero."
    return "OK"

def check_duplicate_declaration(tabela_simbolos, var_name):
    result = tabela_simbolos.lookup(var_name)
    if isinstance(result, dict):
        return f"Variável '{var_name}' já foi declarada."
    return "OK"

def check_scope(variable_scope, var_name, current_scope):
    if var_name not in variable_scope.get(current_scope, set()):
        return f"Variável '{var_name}' fora do escopo."
    return "OK"

def sintatico(token_array, lines, lexemas):
    tokens = np.array(token_array)
    producoes = getProducoes()
    tabParsing = getTabParsing()
    tabela_simbolos = simbolos.TabelaSimbolos()
    current_scope = 0

    pilha = [51]  # $
    pilha = np.hstack([producoes[0][:], pilha])

    print("Tokens iniciais:", tokens)
    print("Pilha inicial:", pilha)

    X = pilha[0]
    a = tokens[0]
    current_line = lines[0]
    current_lexema = lexemas[0]

    while X != 51:  # $
        print("Pilha:", pilha)
        print("X:", X)
        print("a:", a)
        
        if X == 17 or X == -1:  # Vazio
            pilha = np.delete(pilha, [0])
            if pilha.size != 0:
                X = pilha[0]
            else:
                X = 51  # Fim da pilha
            continue

        # Semantic actions
        elif X == 9:  # Token for 'program'
            name = lexemas[1]
            result = check_duplicate_declaration(tabela_simbolos, name)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break
            tabela_simbolos.insert(name, 'program', None, current_scope)

        elif X == 10:  # Token for 'procedure'
            name = lexemas[1]
            type = lexemas[3]
            result = check_duplicate_declaration(tabela_simbolos, name)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break
            tabela_simbolos.insert(name, 'procedure', type, current_scope)
            
        elif X == 22:  # Token for 'declaravariaveis'
            i = 1
            while tokens[i] != 42:  # Token for ';'
                if tokens[i] == 16:  # Token for 'identificador'
                    name = lexemas[i]
                    if tokens[i + 1] == 43:  # Token for ':'
                        type = lexemas[i + 2]
                        result = check_duplicate_declaration(tabela_simbolos, name)
                        if result != "OK":
                            print(f'Semantic Error: {result} at line {current_line}')
                            break
                        tabela_simbolos.insert(name, 'variable', type, current_scope)
                        i += 3  # Skip 'identificador', ':', and 'type'
                    elif tokens[i + 1] == 47:  # Token for ','
                        while tokens[i] == 47:  # Handle multiple identifiers
                            name = lexemas[i - 1]
                            result = check_duplicate_declaration(tabela_simbolos, name)
                            if result != "OK":
                                print(f'Semantic Error: {result} at line {current_line}')
                                break
                            tabela_simbolos.insert(name, 'variable', type, current_scope)
                            i += 2  # Skip ',' and next 'identificador'
                        type = lexemas[i + 1]
                        result = check_duplicate_declaration(tabela_simbolos, lexemas[i])
                        if result != "OK":
                            print(f'Semantic Error: {result} at line {current_line}')
                            break
                        tabela_simbolos.insert(lexemas[i], 'variable', type, current_scope)
                        i += 2  # Skip 'identificador' and 'type'
                else:
                    i += 1

        elif X == 23:  # Token for 'const'
            i = 1
            while tokens[i] != 42:  # Token for ';'
                if tokens[i] == 16:  # Token for 'identificador'
                    name = lexemas[i]
                    if tokens[i + 1] == 31:  # Token for '='
                        type = lexemas[i + 2]
                        result = check_duplicate_declaration(tabela_simbolos, name)
                        if result != "OK":
                            print(f'Semantic Error: {result} at line {current_line}')
                            break
                        tabela_simbolos.insert(name, 'const', type, current_scope)
                        i += 3  # Skip 'identificador', '=', and 'type'
                    elif tokens[i + 1] == 47:  # Token for ','
                        while tokens[i] == 47:  # Handle multiple identifiers
                            name = lexemas[i - 1]
                            result = check_duplicate_declaration(tabela_simbolos, name)
                            if result != "OK":
                                print(f'Semantic Error: {result} at line {current_line}')
                                break
                            tabela_simbolos.insert(name, 'const', type, current_scope)
                            i += 2  # Skip ',' and next 'identificador'
                        type = lexemas[i + 1]
                        result = check_duplicate_declaration(tabela_simbolos, lexemas[i])
                        if result != "OK":
                            print(f'Semantic Error: {result} at line {current_line}')
                            break
                        tabela_simbolos.insert(lexemas[i], 'const', type, current_scope)
                        i += 2  # Skip 'identificador' and 'type'
                else:
                    i += 1

        elif X == 16:  # Token for 'identificador'
            result = check_variable_declared(tabela_simbolos, current_lexema)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break
            symbol = tabela_simbolos.lookup(current_lexema)
            if isinstance(symbol, str):  # Error message returned
                print(f'Semantic Error: {symbol} at line {current_line}')
                break
            if symbol['category'] == 'const' and tokens[1] == 31 and X != 23:  # Token for '=' and not in const declaration
                if tokens[2] != 5 and tokens[2] != 7 and tokens[2] != 14 and tokens[2] != 24 and tokens[2] != 27: # Token for 'string', 'real', 'integer', 'char' or array
                    print(f'Semantic Error: Cannot assign to constant {current_lexema} at line {current_line}')
                    break

        elif X == 5 and X == 7 and X == 14 and X == 24 and X == 27: # Token for 'string', 'real', 'integer', 'char' or 'array'
            var_name = lexemas[1]
            result = check_duplicate_declaration(tabela_simbolos, var_name)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break
            tabela_simbolos.insert(var_name, 'var', lexemas[3], current_scope)

        elif X == 44:  # Token for 'TERMO'
            if tokens[1] == 44:  # Token for '/'
                result = check_division_by_zero(tokens[2])
                if result != "OK":
                    print(f'Semantic Error: {result} at line {current_line}')
                    break

        elif X == 68:  # Token for 'EXPRESSAO'
            var1 = lexemas[1]
            var2 = lexemas[3]
            operation = lexemas[2]
            result = check_data_types(var1, var2, operation)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break

        # Check for multiple declarations in the same line
        if X == 42 and tokens[1] == 16:  # Token for ';' and next token is 'identificador'
            name = lexemas[1]
            type = lexemas[3]
            result = check_duplicate_declaration(tabela_simbolos, name)
            if result != "OK":
                print(f'Semantic Error: {result} at line {current_line}')
                break
            tabela_simbolos.insert(name, 'variable', type, current_scope)

        # Update current_lexema for the next iteration
        if len(lexemas) != 0:
            current_lexema = lexemas[0]

        if X <= 52:  # X é terminal
            if X == a:
                pilha = np.delete(pilha, [0])
                tokens = np.delete(tokens, [0])
                lines = np.delete(lines, [0])
                lexemas = np.delete(lexemas, [0])
                if tokens.size != 0:
                    a = tokens[0]
                    current_line = lines[0]
                    current_lexema = lexemas[0]
                else:
                    a = 51  # Fim da entrada
                if pilha.size != 0:
                    X = pilha[0]
                else:
                    X = 51  # Fim da pilha
            else:
                print(f'Error: Unexpected token {a} at line {current_line}')
                break
        else:  # X é não terminal
            if tabParsing[X][a] != 0:
                producao = producoes[tabParsing[X][a] - 1]
                pilha = np.delete(pilha, [0])
                pilha = np.hstack([producao[producao != -1], pilha])
                X = pilha[0]
            else:
                print(f'Error: No production found for {X} and {a} at line {current_line}')
                break

    if X == 51 and a == 51:
        print("Parsing completed successfully.")
    else:
        print("Parsing failed.")
