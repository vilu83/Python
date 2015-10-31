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
        libros = set()               #Conjunto vacio que va a contener los libros que ha calificado el usuario
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
        
def estimacion_rating (usuarioA, libro):
#Rating Diccionario[Usuario] = [(Libro, Rating),...]
#sumatioria de correlacion(entre usuarioA y usuarioB)*rating(usiarioA,para ese libro)
#todo dividido por sumato del valor absoluto de la correlacion entre ua y usuario i
    r_parcial1 = 0
    r_parcial2 = 0
    for usr in ratings.keys():  #se itera sobre cada usuario
        if usr != usuarioA:
            for book in ratings[usr]:
                if libro == book[0]:
                    r_parcial1 += (float(correlacion(usuarioA, usr)*ratings[usr][1]))
                    r_parcial2 += (float(abs(correlacion(usuarioA,usr))))
    resultado = (r_parcial1/r_parcial2)
    return resultado

def allBooksData():                                            #Retorna Conjunto el ISBN todos los Libros Registrados y un diccionario de forma {ISBN: ("Nombre","Autor","Anno de Publicacion","Editorial"}
    librosF = open("BX-Books.csv")
    libros = set()
    dataLibros = {}
    pLinea = True                                           #Ignorar primera linea del csv
    for lineaLibro in librosF:
        if not pLinea:
            dataLibro = lineaLibro.strip().split(';')
            libros.add(dataLibro[0])
            dataLibros[dataLibro[0]] = (dataLibro[1],dataLibro[2],dataLibro[3],dataLibro[4])
        pLinea = False
    librosF.close()
    return libros, dataLibros

#Retorna una lista con las llaves del diccionario ordenadas segun su valor de menor a mayor mediante el Bubble Sort
def ordenar(diccionario):
    orden = diccionario.keys()
    for elemento in orden:
        for i in range(len(orden)-1):
            if diccionario[orden[i]] < diccionario[orden[i+1]]:
                aux = orden[i]
                orden[i] = orden[i+1]
                orden[i+1] = aux
    return orden

def topLibros(usuario):
    allBooks, dataBooks = allBooksData()
    librosLeidos, librosRating = LibrosUsuario(usuario)
    librosNoLeidos = allBooks - librosLeidos
    ratingEstimadoLibros = {}                            #Diccionario de la forma {isbn:ratingEstimado}
    for book in librosNoLeidos:
        ratingEstimadoLibros[book] = estimacion_rating(usuario,book)
        top = ordenar(ratingEstimadoLibros)
    return top

## Crear Diccionario que tenga los datos del archivo BX-Book_Ratings.csv ##

archivoratings=open("BX-Book-Ratings.csv")                  #Abre el archivo especificado
ratings = {}                                                #Crea un diccionario vacio que sera de la forma Diccionario[Usuario] = [(Libro, Rating),...]. Esto es para no tener que recorrer el archivo de texto mas de una vez.
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

## Ingreso de Usuario ##

userID = raw_input("Ingrese el ID del Usuario al cual recomendarle libros: ")
k = int(raw_input("Ingrese cuantos libros desea recomendar: "))

## Codigo Principal ##

topk = topLibros(userID)[:k]
allBooks, bookData = allBooksData()
print "Te Recomendamos los siguientes libros:"
recomendacion = "{0}. {1} de {2} del anno {3}, publicado por {4}"
for indLibroR in range(len(topk)):
    isbn = topk[indLibroR]
    nombre, autor, anno, editorial = bookData[isbn]
    print recomendacion.format(indLibroR, nombre, autor, anno, editorial)

print 'Gracias por usar este programa ^.^'
	
