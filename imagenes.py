def  escaladeMrgrey (matriz)
	for pixely in matriz:
		for pixelx in matriz:
			red, green, blue = pixelx[pixely][0]
			gris = (red+green+blue)/3
			valorRGBnew = [gris, gris, gris]
			pixey[pixelx] = valorRGBnew
