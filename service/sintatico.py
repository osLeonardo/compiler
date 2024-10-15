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
    # Inicializando a tabela de parsing com zeros
    tabParsing = np.zeros((82, 53))  # 82 estados não terminais, 53 tokens terminais

    # Exemplo de preenchimento da tabela de parsing
    tabParsing[53][9] = 1  # Estado <PROGRAMA>, token "program" -> Produção 0
    tabParsing[54][23] = 2  # Estado <BLOCO>, token "const" -> Produção 2
    tabParsing[54][22] = 2  # Estado <BLOCO>, token "declaravariaveis" -> Produção 2
    tabParsing[54][10] = 2  # Estado <BLOCO>, token "procedure" -> Produção 2
    tabParsing[54][26] = 2  # Estado <BLOCO>, token "begin" -> Produção 2
    tabParsing[55][10] = 3  # Estado <DCLPROC>, token "procedure" -> Produção 22
    tabParsing[55][17] = 4  # Estado <DCLPROC>, token "î" -> Produção 23
    tabParsing[56][23] = 5  # Estado <DCLCONST>, token "const" -> Produção 2
    tabParsing[56][17] = 6  # Estado <DCLCONST>, token "î" -> Produção 3
    tabParsing[57][22] = 7  # Estado <DCLVAR>, token "declaravariaveis" -> Produção 6
    tabParsing[57][17] = 8  # Estado <DCLVAR>, token "î" -> Produção 7
    tabParsing[58][26] = 9  # Estado <CORPO>, token "begin" -> Produção 26
    tabParsing[59][18] = 10  # Estado <TIPO>, token "integer" -> Produção 18
    tabParsing[59][24] = 11  # Estado <TIPO>, token "char" -> Produção 19
    tabParsing[59][5] = 12  # Estado <TIPO>, token "string" -> Produção 20
    tabParsing[59][7] = 13  # Estado <TIPO>, token "real" -> Produção 21
    tabParsing[59][27] = 14  # Estado <TIPO>, token "array" -> Produção 13
    tabParsing[60][16] = 15  # Estado <LDCONST>, token "identificador" -> Produção 4
    tabParsing[60][17] = 16  # Estado <LDCONST>, token "î" -> Produção 5
    tabParsing[61][16] = 17  # Estado <LID>, token "identificador" -> Produção 8
    tabParsing[62][16] = 18  # Estado <LDVAR>, token "identificador" -> Produção 11
    tabParsing[62][17] = 19  # Estado <LDVAR>, token "î" -> Produção 12
    tabParsing[63][47] = 20  # Estado <REPIDENT>, token "," -> Produção 9
    tabParsing[63][17] = 21  # Estado <REPIDENT>, token "î" -> Produção 10
    tabParsing[64][18] = 22  # Estado <TIPOARRAY>, token "integer" -> Produção 14
    tabParsing[64][24] = 23  # Estado <TIPOARRAY>, token "char" -> Produção 15
    tabParsing[64][5] = 24  # Estado <TIPOARRAY>, token "string" -> Produção 16
    tabParsing[64][7] = 25  # Estado <TIPOARRAY>, token "real" -> Produção 17
    tabParsing[65][50] = 26  # Estado <DEFPAR>, token "(" -> Produção 24
    tabParsing[65][17] = 27  # Estado <DEFPAR>, token "î" -> Produção 25
    tabParsing[66][15] = 28  # Estado <COMANDO>, token "if" -> Produção 29
    tabParsing[66][1] = 29  # Estado <COMANDO>, token "while" -> Produção 30
    tabParsing[66][6] = 30  # Estado <COMANDO>, token "repeat" -> Produção 31
    tabParsing[66][8] = 31  # Estado <COMANDO>, token "read" -> Produção 32
    tabParsing[66][25] = 32  # Estado <COMANDO>, token "chamaprocedure" -> Produção 33
    tabParsing[66][0] = 33  # Estado <COMANDO>, token "write" -> Produção 34
    tabParsing[66][18] = 34  # Estado <COMANDO>, token "for" -> Produção 35
    tabParsing[66][17] = 35  # Estado <COMANDO>, token "î" -> Produção 36
    tabParsing[67][15] = 36  # Estado <REPCOMANDO>, token "if" -> Produção 27
    tabParsing[67][1] = 37  # Estado <REPCOMANDO>, token "while" -> Produção 27
    tabParsing[67][6] = 38  # Estado <REPCOMANDO>, token "repeat" -> Produção 27
    tabParsing[67][8] = 39  # Estado <REPCOMANDO>, token "read" -> Produção 27
    tabParsing[67][25] = 40  # Estado <REPCOMANDO>, token "chamaprocedure" -> Produção 27
    tabParsing[67][0] = 41  # Estado <REPCOMANDO>, token "write" -> Produção 27
    tabParsing[67][18] = 42  # Estado <REPCOMANDO>, token "for" -> Produção 27
    tabParsing[67][20] = 43  # Estado <REPCOMANDO>, token "end" -> Produção 28
    tabParsing[68][16] = 44  # Estado <EXPRESSAO>, token "identificador" -> Produção 43
    tabParsing[68][37] = 45  # Estado <EXPRESSAO>, token "numinteiro" -> Produção 43
    tabParsing[68][36] = 46  # Estado <EXPRESSAO>, token "numreal" -> Produção 43
    tabParsing[68][38] = 47  # Estado <EXPRESSAO>, token "nomestring" -> Produção 43
    tabParsing[68][39] = 48  # Estado <EXPRESSAO>, token "nomechar" -> Produção 43
    tabParsing[68][50] = 49  # Estado <EXPRESSAO>, token "(" -> Produção 43
    tabParsing[69][20] = 50  # Estado <ELSEPARTE>, token "else" -> Produção 69
    tabParsing[69][17] = 51  # Estado <ELSEPARTE>, token "î" -> Produção 70
    tabParsing[70][16] = 52  # Estado <VARIAVEL>, token "identificador" -> Produção 71
    tabParsing[71][47] = 53  # Estado <REPVARIAVEL>, token "," -> Produção 72
    tabParsing[71][49] = 54  # Estado <REPVARIAVEL>, token ")" -> Produção 73
    tabParsing[72][50] = 55  # Estado <PARAMETROS>, token "(" -> Produção 37
    tabParsing[72][17] = 56  # Estado <PARAMETROS>, token "î" -> Produção 38
    tabParsing[73][13] = 57  # Estado <ITEMSAIDA>, token "literal" -> Produção 39
    tabParsing[73][16] = 58  # Estado <ITEMSAIDA>, token "identificador" -> Produção 40
    tabParsing[73][37] = 59  # Estado <ITEMSAIDA>, token "numinteiro" -> Produção 40
    tabParsing[73][36] = 60  # Estado <ITEMSAIDA>, token "numreal" -> Produção 40
    tabParsing[73][38] = 61  # Estado <ITEMSAIDA>, token "nomestring" -> Produção 40
    tabParsing[73][39] = 62  # Estado <ITEMSAIDA>, token "nomechar" -> Produção 40
    tabParsing[73][50] = 63  # Estado <ITEMSAIDA>, token "(" -> Produção 40
    tabParsing[74][47] = 64  # Estado <REPITEM>, token "," -> Produção 41
    tabParsing[74][49] = 65  # Estado <REPITEM>, token ")" -> Produção 42
    tabParsing[75][16] = 66  # Estado <TERMO>, token "identificador" -> Produção 44
    tabParsing[75][37] = 67  # Estado <TERMO>, token "numinteiro" -> Produção 44
    tabParsing[75][36] = 68  # Estado <TERMO>, token "numreal" -> Produção 44
    tabParsing[75][38] = 69  # Estado <TERMO>, token "nomestring" -> Produção 44
    tabParsing[75][39] = 70  # Estado <TERMO>, token "nomechar" -> Produção 44
    tabParsing[75][50] = 71  # Estado <TERMO>, token "(" -> Produção 44
    tabParsing[76][35] = 72  # Estado <REPEXP>, token "+" -> Produção 61
    tabParsing[76][52] = 73  # Estado <REPEXP>, token "-" -> Produção 62
    tabParsing[76][11] = 74  # Estado <REPEXP>, token "or" -> Produção 63
    tabParsing[76][4] = 75  # Estado <REPEXP>, token "then" -> Produção 64
    tabParsing[76][21] = 76  # Estado <REPEXP>, token "do" -> Produção 64
    tabParsing[76][2] = 77  # Estado <REPEXP>, token "until" -> Produção 64
    tabParsing[76][3] = 78  # Estado <REPEXP>, token "to" -> Produção 64
    tabParsing[76][47] = 79  # Estado <REPEXP>, token "," -> Produção 64
    tabParsing[76][49] = 80  # Estado <REPEXP>, token ")" -> Produção 64
    tabParsing[76][40] = 81  # Estado <REPEXP>, token "]" -> Produção 64
    tabParsing[76][41] = 82  # Estado <REPEXP>, token "[" -> Produção 64
    tabParsing[77][31] = 83  # Estado <REPEXPSIMP>, token "=" -> Produção 51
    tabParsing[77][33] = 84  # Estado <REPEXPSIMP>, token "<>" -> Produção 52
    tabParsing[77][30] = 85  # Estado <REPEXPSIMP>, token ">" -> Produção 53
    tabParsing[77][29] = 86  # Estado <REPEXPSIMP>, token ">=" -> Produção 54
    tabParsing[77][34] = 87  # Estado <REPEXPSIMP>, token "<=" -> Produção 55
    tabParsing[77][32] = 88  # Estado <REPEXPSIMP>, token "<" -> Produção 56
    tabParsing[77][4] = 89  # Estado <REPEXPSIMP>, token "then" -> Produção 57
    tabParsing[77][21] = 90  # Estado <REPEXPSIMP>, token "do" -> Produção 57
    tabParsing[77][2] = 91  # Estado <REPEXPSIMP>, token "until" -> Produção 57
    tabParsing[77][3] = 92  # Estado <REPEXPSIMP>, token "to" -> Produção 57
    tabParsing[77][47] = 93  # Estado <REPEXPSIMP>, token "," -> Produção 57
    tabParsing[77][49] = 94  # Estado <REPEXPSIMP>, token ")" -> Produção 57
    tabParsing[77][40] = 95  # Estado <REPEXPSIMP>, token "]" -> Produção 57
    tabParsing[77][41] = 96  # Estado <REPEXPSIMP>, token "[" -> Produção 57
    tabParsing[78][16] = 97  # Estado <FATOR>, token "identificador" -> Produção 46
    tabParsing[78][37] = 98  # Estado <FATOR>, token "numinteiro" -> Produção 45
    tabParsing[78][36] = 99  # Estado <FATOR>, token "numreal" -> Produção 49
    tabParsing[78][38] = 100  # Estado <FATOR>, token "nomestring" -> Produção 47
    tabParsing[78][39] = 101  # Estado <FATOR>, token "nomechar" -> Produção 48
    tabParsing[78][50] = 102  # Estado <FATOR>, token "(" -> Produção 50
    tabParsing[79][48] = 103  # Estado <REPTERMO>, token "*" -> Produção 65
    tabParsing[79][44] = 104  # Estado <REPTERMO>, token "/" -> Produção 66
    tabParsing[79][28] = 105  # Estado <REPTERMO>, token "and" -> Produção 67
    tabParsing[79][4] = 106  # Estado <REPTERMO>, token "then" -> Produção 68
    tabParsing[79][21] = 107  # Estado <REPTERMO>, token "do" -> Produção 68
    tabParsing[79][2] = 108  # Estado <REPTERMO>, token "until" -> Produção 68
    tabParsing[79][3] = 109  # Estado <REPTERMO>, token "to" -> Produção 68
    tabParsing[79][47] = 110  # Estado <REPTERMO>, token "," -> Produção 68
    tabParsing[79][49] = 111  # Estado <REPTERMO>, token ")" -> Produção 68
    tabParsing[79][40] = 112  # Estado <REPTERMO>, token "]" -> Produção 68
    tabParsing[79][41] = 113  # Estado <REPTERMO>, token "[" -> Produção 68
    tabParsing[80][35] = 114  # Estado <EXPSIMP>, token "+" -> Produção 58
    tabParsing[80][52] = 115  # Estado <EXPSIMP>, token "-" -> Produção 59
    tabParsing[80][16] = 116  # Estado <EXPSIMP>, token "identificador" -> Produção 60
    tabParsing[80][37] = 117  # Estado <EXPSIMP>, token "numinteiro" -> Produção 60
    tabParsing[80][36] = 118  # Estado <EXPSIMP>, token "numreal" -> Produção 60
    tabParsing[80][38] = 119  # Estado <EXPSIMP>, token "nomestring" -> Produção 60
    tabParsing[80][39] = 120  # Estado <EXPSIMP>, token "nomechar" -> Produção 60
    tabParsing[80][50] = 121  # Estado <EXPSIMP>, token "(" -> Produção 60

    return tabParsing

def sintatico(token_array):
    # Variável para armazenar o array de tokens (que irá alimentar o sintático)
    tokens = np.array(token_array)

    # Obter produções e tabela de parsing
    producoes = getProducoes()
    tabParsing = getTabParsing()

    pilha = [51]  # $

    # Empilhar a primeira produção (P0: <PROGRAMA>)
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
                    if tokens.size != 0:
                        a = tokens[0]
                    else:
                        a = 51  # Fim da entrada
                    if pilha.size != 0:
                        X = pilha[0]
                    else:
                        X = 51  # Fim da pilha
                else:
                    print('Error: Unexpected token')
                    break
            else:  # Não terminal
                if tabParsing[X][a] != 0:
                    producao = producoes[int(tabParsing[X][a]) - 1]
                    pilha = np.delete(pilha, [0])
                    if producao[0] != 17:  # Não é vazio
                        pilha = np.hstack([producao, pilha])
                    X = pilha[0]
                else:
                    print('Error: No production found')
                    break

    if X == 51 and a == 51:
        print('Parsing completed successfully')
    else:
        print('Error: Parsing did not complete successfully')