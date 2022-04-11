import symbolsTable as sym 
#Variables globales para la entrada y salida de archivos
INPUT_FILE = 'fuente.txt'
OUTPUT_FILE = 'testout.txt'
EOF=''

#Invocamos el metodo main para dar inicio al analizador lexico
def main():
    #Leemos la tabla de simbolos e invocamos la apertura del archivo
    table = sym.SymbolTable()
    openFille()
    with open(INPUT_FILE) as dataFile:
        fileProcess(dataFile,table)
    dataFile.close()

def fileProcess(dataFile,table):
    dataCharacter = '1'
    token = ''
    line = ''
    numLine = 1
    dataCharacter = dataFile.readline(1)
    tabs = 0
    while (dataCharacter != EOF) :
        try:
            if (dataCharacter == '\n') :
                writeLine(line + '\n')
                line = '' + ("\t"*tabs)
                numLine += 1
                dataCharacter = dataFile.readline(1)
                continue
            elif (dataCharacter == ' '):
                dataCharacter = dataFile.readline(1)
                continue
            elif (dataCharacter == EOF):
                break
                
            elif (dataCharacter.lower() == 'f' or dataCharacter.lower() == 't') : 
                #quiere decir que lo mas probable es que venga un falso
                token = table.searchKey(booleanData(dataFile,dataCharacter))
            else:
                token = table.searchKey(dataCharacter)
                if(token.number==sym.LIT_STRING):
                    stringData(dataFile)
                elif(token.number==sym.LIT_NUMBER):
                    numberData(dataFile)
                elif(token.number==sym.L_SQUAREBRACKET or token.number == sym.L_BRACKET):
                    tabs+=1
                elif(token.number==sym.R_SQUAREBRACKET or token.number == sym.R_BRACKET):
                    tabs-=1

            line += token.tokenName + ' '
            dataCharacter = dataFile.readline(1)
        except Exception as error:
            # line += token.nombre_token + ' '
            writeLine(line + '\n')
            print(error)
            exit(-1)

def stringData(dataFile):
    while (True):
        dataCharacter = dataFile.readline(1)
        if (dataCharacter == '"'):
            return "STRING"
        if(dataCharacter == EOF):
            raise Exception("Archivo terminado sin cerrar cadena")

def numberData(dataFile):
    while (True):
        dataCharacter = dataFile.readline(1)
        if ((dataCharacter == '' or dataCharacter == '\n' or dataCharacter == ',') and (True)) : 
            #Condicion para que siempre encuentre numeros, caso contrario devuelve error
            return 'NUMBER'
            break
    pass


def booleanData(dataFile,dataCharacter):
    lista = [['f','a','l','s','e'],['t','r','u','e']]
    dataBoolean = dataCharacter
    while (True) :
        dataCharacter = dataFile.readline(1)
        dataBoolean += dataCharacter
        if (dataCharacter=='e' ):
            break
    if(dataBoolean == 'false'):
        return 'false'
    if(dataBoolean =='true'):
        return 'true'
    raise Exception ("Error,booleano mal escrito")

    pass

def writeLine(line):
    with open(OUTPUT_FILE,'a') as outline :
        outline.write(line)
    outline.close()

def openFille():
    with open(OUTPUT_FILE,'w') as outline :
        print("")
    outline.close()

main()