# -*- coding: cp1252 -*-
#Juan Pablo San Martin
#Patricio Campaña
#Tomas Cantuarias

#Importar funciones para Graficar y revisar archivos
import matplotlib.pyplot as plt
import os

#Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
def histoParrafo(parrafo):
    #Eliminar Signos de Puntuacion
    for punt in [',','.','#',';','$','%','&','\/','(',')','=','\"','\'',':']:
        parrafo = parrafo.replace(punt,'')
    #Convertir a Minuscula, eliminar \n y volver una lista el parrafo
    palabras = parrafo.lower().strip().split()
    #Crear Histograma en un diccionario
    histograma = {}
    for palabra in palabras:
        if palabra not in histograma.keys():
            histograma[palabra] = palabras.count(palabra)           
    return histograma

#Retorna un conjunto con todas las palabras de ambos parrafos y completa los histogramas con las palabras que no aparecen en los parrafos
def vocabulario(histograma1,histograma2):
    vocab = set()
    for palabra in histograma1:
        vocab.add(palabra)
    for palabra in histograma2:
        vocab.add(palabra)
    return vocab

#Funcion que calcula la distancia euclidiana a partir de los diccionarios con las frecuencias de las palabras. Usar diccionario vacio para deu(h1,0)
def distEuclidiana(histograma1, histograma2):
    #Obtener conjunto con todas las palabras
    vocab = vocabulario(histograma1, histograma2)
    #Sumar la cantidad de palabras diferentes
    suma = 0
    for palabra in vocab:
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma1:
            palabraR1 = 0
        else:
            palabraR1 = histograma1[palabra]
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma2:
            palabraR2 = 0
        else:
            palabraR2 = histograma2[palabra]
        suma += (palabraR1 - palabraR2) ** 2
    return suma ** 0.5

#Funcion que calcula la distancia Coseno de dos Histogramas
def distCoseno(histograma1,histograma2):
    #Guarda las distancias Euclidianas de ambos histogramas
    distE1 = distEuclidiana(histograma1,{})
    distE2 = distEuclidiana(histograma2,{})
    suma = 0
    vocab = vocabulario(histograma1, histograma2)
    for palabra in vocab:
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma1:
            palabraR1 = 0
        else:
            palabraR1 = histograma1[palabra]
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma2:
            palabraR2 = 0
        else:
            palabraR2 = histograma2[palabra]
        suma += palabraR1 * palabraR2
    return abs(round(1 - (suma/(distE1*distE2)),12))

menu = {
    's':True,
    'S':True,
    'n':False,
    'N':False,
    }

flog = True
while flog:
    Narch = raw_input("Desea comparar 1 o 2 archivos? ")    #Pregunta al usuario si desea comparar 1 o 2 archivos
    if Narch == '1' or Narch == '2':
        flog = False
    elif Narch == "tito":                                   #???
        print 'Usted ha encontrado el Easter Egg'
        os.system('ludo.py')
    else:
        print "Ingrese un comando valido (1 o 2)"

flog = True
while flog:
    a = raw_input("Ingrese nombre archivo 1 aqui (Sin .txt): ")
    if os.path.isfile(a + '.txt'):
        flog = False
    else:
        print a + '.txt No Existe en este directorio'

if Narch == '2':
    flog = True
    while flog:
        b = raw_input("Ingrese nombre archivo 2 aqui (Sin .txt): ") #Si se desea comparar dos archivos, pide el nombre del segundo archivo
        if os.path.isfile(b + '.txt'):
            flog = False
        else:
            print b + '.txt No Existe en este directorio'    
else:
    b = a                                                       #Si se desea comparar un archivo, esta variable se iguala al nombre del archivo
fleg = True
while fleg:
    PS = raw_input("Ingrese el porcentaje de similitud segun el cual considera que hay plagio (0 - 100): ")  #Pregunta al usuario el porcentaje de similitud minimo
    if PS not in str(range(0,100)) or PS == "":
        print "Ingrese un comando valido"
    else:
        fleg = False
        PS = int(PS)
           
archivo1 = open(a + '.txt')
nParr1 = 0                                              ##Permite saber que parrafo se esta revisando del Archivo 1
conflictos = []
porcentajes = []
revisado = []
for parrafo1 in archivo1:
    if parrafo1 != "\n":                                ##Comprueba que el parrafo no sea solo un salto de linea
        nParr1 += 1     
        histo1 = histoParrafo(parrafo1)
        archivo2 = open(b + '.txt')
        nParr2 = 0                                      ##Permite saber que parrafo se esta revisando del Archivo 1
        for parrafo2 in archivo2:
            if parrafo2 != "\n":                        ##Comprueba que el parrafo no sea solo un salto de linea
                nParr2 += 1
                if nParr2 not in revisado:
                    if Narch == '2' or Narch == '1' and nParr1 != nParr2:
                        histo2 = histoParrafo(parrafo2)
                        distE = distEuclidiana(histo1, histo2)          #Distancia Euclidiana entre Parrafo1 y Parrafo2
                        distC = distCoseno(histo1, histo2)              #Distancia Coseno entre Parrafo1 y Parrafo2
                        porcentaje = 100 - (round(distC,2) * 100)       #Calcula porcentaje de similitud entre ambos parrafos
                        if porcentaje >= PS:                            #Si el porcentaje es mayor al valor dado por el usuario, se agrega a la lista de parrafos en conflicto
                            conflictos.append((nParr1,nParr2,porcentaje))
                            porcentajes.append(porcentaje)
    archivo2.close()
    if Narch == '1':
        revisado.append(nParr1)
archivo1.close()

if len(porcentajes) >= 1:
    print "Los parrafos en conflicto son:"                    #Imprime todos los parrafos en conflicto
    for i in conflictos:
        parra1, parra2, porcen = i
        print "Los parrafos", str(parra1), "y", str(parra2), "con un", str(porcen),"% de similitud."
    #Mostrar Grafico de Parrafos en Conflicto
    flog = True
    if len(porcentajes) > 1:
        while flog:
            eleccion = raw_input("Desea Imprimir el Histograma de los Parrafos en Conflicto? (S/N): ")
            if eleccion in menu.keys():
                flog = False
            else:
                print "Ingrese solo 'S' o 'N'"
        if menu[eleccion]:
            plt.title("Frecuencia de porcentajes de similitud entre parrafos en conflicto")
            plt.grid(True)
            plt.hist(porcentajes)
            plt.xlabel("Porcentajes")
            plt.ylabel("Frecuencia")
            plt.show()
    else:
        print "No se puede producir histograma con solo un conflicto"
else:
    print "No hay parrafos en conflicto"    
