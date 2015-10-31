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
    libros1 = set()
    libros2= set()
    usu1 = {}
    usu2 = {}
    for tupla in ratings[usuario1]:
        libro, rating = tupla
        libros1.add(libro)
        
        

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
