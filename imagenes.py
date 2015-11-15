# -*- coding: cp1252 -*-
from PIL import Image
from funciones import *
import numpy as np
import os

def abrirArchivo(nombreArchivo):
	if sys.platform == 'linux2':
    		subprocess.call(["xdg-open", nombreArchivo])
	else:
    		os.startfile(nombreArchivo)

def ArrayAImagen(arr, nombreSalida):
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
	im.save(nombreSalida)
	abrirArchivo(nombreSalida)
	return True

def espejovertical(matriz):
	espejov = np.array(matriz)[::-1]
	salida = nombre+"EspejoVertical.png"
	ArrayAImagen(espejov, salida)

def espejo(matriz):
    espejo = np.array(matriz)
    espejo = np.fliplr(espejo)
    salida = nombre+"Espejo.png"
    ArrayAImagen(espejo, salida)
    

def  escaladeMrgrey (matriz):
        for pixely in matriz:
            for pixelx in matriz:
                red, green, blue = pixelx[pixely][0]
                gris = (red+green+blue)/3
                valorRGBnew = [gris, gris, gris]
                pixely[pixelx] = valorRGBnew
        salida = nombre+"EDG.png"
        convertirMatrizAImagen(matriz, salida)
        abrirArchivo(salida)


def rotar(imagenMatriz, rotacion):	#1=90[grado],2=180[grado],3=270[grado]
	imagenMatriz = numpy.rot90(numpy.array(imagenMatriz),rotacion)
	salida = nombre+"Rotacion"+str(rotacion*90)+".png"
	ArrayAImagen(imagenMatriz, salida)


def negativo(matriz):
    matriz1 = matriz
    for filaPix in matriz1:
        for pix in filaPix:
            for color in range(3):
                pix[color] = 255 - pix[color]
    salida = nombre+"Negativo.png"
    convertirMatrizAImagen(matriz1, salida)
    abrirArchivo(salida)

nombre = raw_input("Ingrese el nombre de la imagen: ")
tipo = "."+raw_input("Ingrese el tipo de archivo de la imagen: ")
imagen = nombre+tipo
archivo = nombre + ".txt"
convertirImagenAArchivo(imagen, archivo)
matriz = leerArchivo(archivo)
flag = True
dic = {"espejo": espejo,
       "espejovertical": espejovertical,
       "edg": escaladeMrgrey,
       "negativo": negativo}
       
while flag:
    fleg = True
    print "Comandos disponibles:\nespejo : Aplica efecto espejo a la imagen\nespejovertical : Aplica efecto de espejo vertical a la imagen\nedg : Aplica efecto de escala de grises a la imagen\nnegativo: Aplica efecto negativo a la imagen\n90 : Rota la Imagen en 90º\n180: Rota la imagen en 180º\n270 : Rota la imagen en 270º"
    comando = raw_input("Ingrese un comando: ").lower()
    if comando == "" or comando not in ["espejo", "espejovertical", "edg", "negativo", "90", "180", "270"]:
        print "Por favor, ingrese un comando valido"
    else:
        if comando in ["90","180","270"]:
            rotar(matriz, int(comando)/90)
        else:
            dic[comando](matriz)
        while fleg:
            asd = raw_input("Desea realizar otra operacion? (s/n): ").lower()
            if asd not in ["s","n"] or asd == '':
                print "Ingrese un comando valido"
            else:
                fleg = False
                if asd == "n":
                    flag = False
        
    
    
