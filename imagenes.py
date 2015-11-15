from PIL import Image
from funciones import *
import numpy as np
import os

def ArrayAImagen(arr, nombreSalida):
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
	im.save(nombreSalida)
	return True

def espejovertical(matriz):
	espejo = np.array(matriz)[::-1]
	salida = nombre+"espejovertical"+tipo
	ArrayAImagen(espejo, salida)
	os.system(salida)
	
def espejo(matriz):
    espejo = np.array(matriz)
    espejo = np.fliplr(espejo)
    salida = nombre+"espejo"+tipo
    ArrayAImagen(espejo, salida)
    os.system(salida)

def  escaladeMrgrey (matriz):
	for pixely in matriz:
		for pixelx in pixely:
			red, green, blue = pixelx[pixely][0]
			gris = (red+green+blue)/3
			valorRGBnew = [gris, gris, gris]
			pixey[pixelx] = valorRGBnew

def negativo(matriz):
	for filaPix in matriz:
		for pix in filaPix:
			for color in range(3):
				pix[color] = 255 - pix[color]

nombre = raw_input("Ingrese el nombre de la imagen: ")
tipo = raw_input("Ingrese el tipo de archivo de la imagen(inclyendo punto): ")
imagen = nombre+tipo
archivo = nombre + ".txt"
convertirImagenAArchivo(imagen, archivo)
matriz = leerArchivo(archivo)
espejovertical(matriz)
a = raw_input()



