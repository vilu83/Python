#Juan Pablo San Martin
#Patricio Campana
#Tomas Cantuarias

#BX-Book-Ratings.csv --> "User-ID";"ISBN";"Book-Rating"
#BX-Users.csv -->"User-ID";"Location";"Age"
#BX-Books.csv -->"ISBN";"Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"

#Dicc --> polio = {} --> polio[User-ID] = [(ISBN,Book-Rating),...

def LibrosUsuario(usuario):
    for tupla in ratings[usuario]:    #Diccionario donde el usuario es la llave y los valores son una lista de tuplas, con tuplas de la forma (Libro, Rating) 
        usu = {}                      #Diccionario del usuario 1 donde el libro es la llave y el rating el valor
        libros = sset()               #Conjunto vacio que va a contener los libros que ha calificado el usuario
        libro, rating = tupla
        if rating > 0:                #Ignora los libros cuyos rating sean 0
            libros.add(libro)         #Agrega el libro al conjunto de los libros que ha calificado el usuario 
            usu[libro] = rating       #Agrega el libro como llave y el rating como valor al diccionario del usuario    
    return libros, usu

def correlacion(usuario1, usurero):
    libros1, usu1 = LibrosUsuario(usuario1)                   
    libros2, usu2 = LibrosUsuario(usurero)
    MediaUsu1 = sum(usu1.values())/len(usu1.values())         #Media de los ratings del usuario 1, sin contar los ratings 0
    MediaUsu2 = sum(usu2.values())/len(usu2.values())         #Media de los ratings del usuario 2, sin contar los ratings 0
    InterLibros = libros1 & libros2                           #Conjunto producto de la interseccion de los libros que han leido el usuario 1 y el 2
    Sumatoria1 = 0                                            #Sumatoria de la formula de correlacion. Corresponde a la sumatoria que esta por sobre la fraccion
    Sumatoria2 = 0                                            #Sumatoria de la formula de correlacion. Corresponde a la sumatoria que esta a la izquierda, debajo de la fraccion
    Sumatoria3 = 0                                            #Sumatoria de la formula de correlacion. Corresponde a la sumatoria que esta a la derecha, debajo de la fraccion
    for libro in InterLibros:                                 #Recorre el conjunto intersectado
        Sumatoria1 += (usu1[libro] - MediaUsu1) * (usu2[libro] - MediaUsu2)           #Se aplica la formula de correlacion
        Sumatoria2 += (usu1[libro] - MediaUsu1)**2                                    #Se aplica la formula de correlacion
        Sumatoria3 += (usu2[libro] - MediaUsu2)**2                                    #Se aplica la formula de correlacion
    Correlacion = Sumatoria1 / ((Sumatoria2)**0.5 * (Sumatoria3)**0.5)                #Se aplica la formula de correlacion
    return Correlacion                                                                #Retorna el resultado de la formula                         #Retorna el resultado de la formula
        
        

archivoratings=open("BX-Book-Ratings.csv")                  #Abre el archivo especificado
ratings = {}                                                #Crea un diccionario vacío que será de la forma Diccionario[Usuario] = [(Libro, Rating),...]. Esto es para no tener que recorrer el archivo de texto mas de una vez.
numerolinea = 0                                             #Contador de lineas
for linea in archivoratings:                                #Recorre el archivo por lineas
    numerolinea += 1                                        #Suma 1 al contador de lineas
    if numerolinea != 1:                                    #Verifica que no sea la primera linea del archivo, la cual describe la forma del archivo y no tiene ningun dato de utilidad
        linea = linea.replace('"','')                       #Elimina las comillas
        lineamod = linea.strip().split(";")                 #Convierte la linea de string a lista
        usuario, libro, rating = lineamod
        if usuario not in ratings:                          #Si el usuario no esta en el diccionario de ratings,
            ratings[usuario]=[(libro,int(rating))]          #utiliza el usuario como llave y el valor es una lista de tuplas, con las tuplas de forma (Libro, Rating)
        else:                                               #Si el usuario si esta en el diccionario de ratings,
            ratings[usuario].append((libro,int(rating)))    #agrega una nueva tupla de la misma forma a la lista
        if numerolinea > 500:
            break
archivoratings.close()
print ratings
