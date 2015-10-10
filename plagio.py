from matplotlib.pylab import hist, show

def his(linea):                 ##Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
    val = linea.strip().split()
        dic = {}
        for i in val:
            if i not in dic:
                dic[i] = val.count(i)
        return dic

def disteu():
    hihihihohohohohoho
def discos():

            

a = raw_input("Ingrese nombre archivo 1 aqui: ")
b = raw_input("Ingrese nombre archivo 2 aqui: ")

archivo1 = open(a)
for parrafo in archivo1:
    if parrafo != "\n": ##Comprueba que el parrafo no sea solo un salto de linea
        dic1 = his(parrafo)
        archivo2 = open(b)
        for parrafo2 in archivo2:
            if parrafo2 != "\n": ##Comprueba que el parrafo no sea solo un salto de linea
                dic2 = his(parrafo2)
                
        
