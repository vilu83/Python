from matplotlib.pylab import hist, show

def his(linea):                 ##Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
    val = linea.strip().split()
        dic = {}
        for i in val:
            if i not in dic:
                dic[i] = val.count(i)
        return dic

def deu(dat1, dat2):   ##Funcion que calcula la distancia euclidiana a partir de los diccionarios con las frecuencias de las palabras. Usar diccionario vacio para deu(h1,0)
    pal = set()
    for i in dat1:
        pal.add(i)
    for i in dat 2:
        pal.add(i)
    suma = 0
    for i in pal:
        if i not in dat1:
            a = 0
        else:
            a = dat1[i]
        if i not in dat2:
            b = 0
        else:
            b = dat2[i]
        suma += (a - b)**2
    return suma**0.5
    
def dcos():

            

a = raw_input("Ingrese nombre archivo 1 aqui: ")
b = raw_input("Ingrese nombre archivo 2 aqui: ")
archivo1 = open(a)
pt1 = 0                               ##Numero del parrafo del texto 1
for parrafo in archivo1:
    if parrafo != "\n":               ##Comprueba que el parrafo no sea solo un salto de linea
        pt1 += 1                      ## Cada vez que pasa por este punto, cambia de parrafo y se le suma 1 al parrafo actual
        dic1 = his(parrafo)
        archivo2 = open(b)
        pt2 = 0                       ##Numero del parrafo del texto 2
        for parrafo2 in archivo2:
            if parrafo2 != "\n":      ##Comprueba que el parrafo no sea solo un salto de linea
                pt2 += 1              ## Cada vez que pasa por este punto, cambia de parrafo y se le suma 1 al parrafo actual
                dic2 = his(parrafo2)
                dist1 = deu(dic1, dic2)
                dist2 = dcos(dic1, dic2)
                
        
