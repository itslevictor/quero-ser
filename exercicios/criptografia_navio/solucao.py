lista_texto = "10010110111101110101011000000001000101110010011001010111000000010001011101110110010101110011011011110111110101110101011100000011"
lista_exemplo = []
def processa_lista1(lista):
    lista_ordenada = []
    penultimo=""
    ultimo = ""
    contador=0
    contador2=1
    for item in lista:
        contador2+=1
        lista_ordenada.append(item)
        contador+=1
        if(contador == 8):
            ultimo = lista_ordenada[len(lista_ordenada)-1]
            penultimo= lista_ordenada[len(lista_ordenada)-2]
            lista_ordenada[len(lista_ordenada)-1] = penultimo
            lista_ordenada[len(lista_ordenada)-2] = ultimo
            #aletracao
            contador = 0
    return lista_ordenada
    
def processa_lista2(lista):
    lista_ordenada = []
    quatro1= []
    quatro2=[]
    alternador = True
    contador=0
    contadorGeral = 0;
    for item in lista:
        contador +=1
        contadorGeral +=1
        if contador >= 5 : contador = 1
        if (contador < 5 and alternador == True):
            quatro1.append(item)
            if contador == 4 : alternador=False
        elif (contador <5 and alternador == False):
            quatro2.append(item)
            if contador == 4 : alternador=True
        if (contadorGeral%8 == 0):
            lista_ordenada.extend(quatro2)
            lista_ordenada.extend(quatro1)
            quatro1 =[]
            quatro2 = []
            contador = 0
        elif (len(lista)%8 != 0 and ((len(lista)-contadorGeral)<(len(lista)-((len(lista)//8)*8)))):
            lista_ordenada.append(item)
            
    return lista_ordenada
    
def listaParaTexto(lista1):
    texto = ""
    for item in lista1:
        texto+=str(item)
    return texto

def textoParaLista(lista2):
    listaNova = []
    for letra in lista2:
        listaNova.append(letra)
    return listaNova

def textoParaBinario(lista3):
    textoBinario = ""
    contador = 0
    for letra in lista3:
        if (contador == 8):
            textoBinario+=" "
            textoBinario+=letra
            contador = 0
        else:
            textoBinario+=letra
        contador+=1
    return textoBinario
    
def listaParaBinario(lista4):
    listaBinaria = []
    contador = 0
    for letra in lista4:
        contador+=1
        listaMomento = []
        if(contador == 8):
            listaBinaria.extend(listaMomento)
            listaMomento = []
            contador = 0
        else:
            listaMomento.append(letra)
    return listaNova
    
def binarioParaTexto(binario):
    texto = ""
    for i in range(0, len(binario), 8):
        caractereBinario = binario[i:i+8]
        caractereDecimal = int(caractereBinario, 2)
        texto += chr(caractereDecimal)
    return texto


lista_exemplo = processa_lista1(textoParaLista(lista_texto))
print("conversao\n",listaParaTexto(processa_lista2(processa_lista1(textoParaLista(lista_texto)))),"\nVersao sem criptografar","10010110111101110101011000000001000101110010011001010111000000010001011101110110010101110011011011110111110101110101011100000011\n","Versao traduzida\n",binarioParaTexto(listaParaTexto(processa_lista2(processa_lista1(textoParaLista(lista_texto))))))
