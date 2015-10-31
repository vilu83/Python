#Juan Pablo San Martin
#Patricio Campana
#Tomas Cantuarias

#BX-Book-Ratings.csv --> "User-ID";"ISBN";"Book-Rating"
#BX-Users.csv -->"User-ID";"Location";"Age"
#BX-Books.csv -->"ISBN";"Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"

#Dicc --> polio = {} --> polio[User-ID] = [(ISBN,Book-Rating),...

#Juan Pablo San Martin
#Patricio Campana
#Tomas Cantuarias

#BX-Book-Ratings.csv --> "User-ID";"ISBN";"Book-Rating"
#BX-Users.csv -->"User-ID";"Location";"Age"
#BX-Books.csv -->"ISBN";"Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"

#Dicc --> polio = {} --> polio[User-ID] = [(ISBN,Book-Rating),...

def correlacion(usuario1, usurero):
    libros1 = set()  #Conjunto vacio que va a contener los libros que ha calificado el usuario 1
    libros2= set()   #Conjunto vacio que va a contener los libros que ha calificado el usuraio 2
    usu1 = {}        #Diccionario del usuario 1 donde el libro es la llave y el rating el valor
    usu2 = {}        #Diccionario del usuario 2 donde el libro es la llave y el rating el valor
    for tupla in ratings[usuario1]:    #Diccionario donde el usuario es la llave y los valores son una lista de tuplas, con tuplas de la forma (Libro, Rating) 
        libro, rating = tupla
        if rating > 0:                 #Ignora los libros cuyos rating sean 0
            libros1.add(libro)         #Agrega el libro al conjunto de los libros que ha calificado el usuario 1
            usu1[libro] = rating       #Agrega el libro como llave y el rating como valor al diccionario del usuario 1
    for tupla2 in ratings[usurero]:    #Diccionario donde el usuario es la llave y los valores son una lista de tuplas, con tuplas de la forma (Libro, Rating)
        libro2, rating2 = tupla2
        if rating2 > 0:                #Ignora los libros cuyos rating sean 0
            libros2.add(libro2)        #Agrega el libro al conjunto de los libros que ha calificado el usuario 2
            usu2[libro2]= rating2      #Agrega el libro como llave y el rating como valor al diccionario del usuario 1
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
    return Correlacion                                                                #Retorna el resultado de la formula
        
        

archivoratings=open("BX-Book-Ratings.csv")
ratings = {}
numerolinea = 0
for linea in archivoratings:
    numerolinea += 1
    if numero != 1:    
        linea = linea.replace('"','')
        lineamod = linea.strip().split(";")
        usuario, libro, rating = lineamod
        if usuario not in ratings:
            ratings[int(usuario)]=[(libro,int(rating))]
        else:
            ratings[int(usuario)].append((libro,int(rating)))
        if numerolinea > 500:
            break
archivoratings.close()
print ratings
