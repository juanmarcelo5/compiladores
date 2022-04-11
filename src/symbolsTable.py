L_SQUAREBRACKET = 256 #regular expression = [
R_SQUAREBRACKET = 257 #regular expresion = ]
L_BRACKET = 258 #regular expression = {
R_BRACKET  259 #regular expresion = }
POINT = 260 #regular expression = ,
COLON = 261 #regular expression = :
LIT_STRING = 262 #regular expression = " .*"
LIT_NUMBER = 263 #regular expression = [0-9]+(\.[0-9]+)?((e|E)(+|-)?[0-9]+)?
VAL_TRUE= 264 #regular expression = true | TRUE
VAL_FALSE = 265 #regular expression = false | FALSE
VAL_NULL = 266  #regular expresion = null | N
LIT_STRING = 267
LIT_NUMBER = 268


class tokenType :
    #en esta parte se definen el nombre del lexema y el componente lexico
    def __init__(self, token = '',tokenName = '', number = 0):
        self.tokenName = tokenName
        self.number = number
        self.lexema = token
    def __str__(self):
        string = ""
        string = ("nombre token:" + str(self.tokenName) +'\n'+"number:" + str(self.number))
        return string

class Token :
    def __init__(self, stringValue = '', numberValue = 0, tokenType = None):
        self.stringValue = stringValue
        self.numberValue = numberValue
        self.tokenType = tokenType
    def __str__(self):
        string = ""
        string = ("string :" + str (self.stringValue) +'\n'+"number :" + str(self.numberValue) +'\n'+"token type :" + str(self.tokenType))
        return string

class SymbolTable :
    def __init__(self, size = 50) :
        self.table = [
            tokenType('[', 'L_SQUAREBRACKET', L_SQUAREBRACKET),
            tokenType(']','R_SQUAREBRACKET' , R_SQUAREBRACKET),
            tokenType('{', 'L_BRACKET', L_BRACKET),
            tokenType('}','R_BRACKET', R_BRACKET),
            tokenType(',','POINT', POINT),
            tokenType('"','STRING',LIT_STRING  ),
            tokenType('NUMBER','NUMBER',LIT_NUMBER),
            tokenType(':','COLON', COLON),
            tokenType('true','VAL_TRUE', VAL_TRUE),
            tokenType('false','VAL_FALSE',VAL_FALSE),
            tokenType('null','VAL_NULL', VAL_NULL),
        ]
    #metodo de insersion de un simbolo en la tabla
    def pushValue (self, value ):
        i = 0
        while (self.table[i].number != -1) :
            i += 1
            if (i == len(self.table)) :
                i = 0
        self.table[i] = value

    def insertTable(self, token,tokenName, number):
        value = tokenType (token,tokenName, number)
        self.pushValue(value)

    #busca la clave e imprime
    def searchKey (self, key):
        for temp in self.table :
            if(temp.lexema == key ):
                return temp
            if(temp.lexema=="NUMBER" and key.isnumeric()):
                return temp
        if(key !=" " and key !="\n"):
            raise Exception("Caracter no valido encontrado<"+key+">")

