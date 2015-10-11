# Integrantes:
# 19.594.837-2 Isaias Bahamondes
# 19.490.989-6 Juan Pablo San Martin
# 19.488.742-6 Patricio Campana

### Inicio Programa ###

#Importar funciones de Turtle y Random
import turtle
import random

#Medida un Bloque "TurtLudo"
tb = 40

#Crear Tortuga "drawer" y Playground
win = turtle.Screen()
win.setup(17*tb,17*tb)
drawer = turtle.Turtle()
drawer.shape('turtle')
drawer.speed(0)

### Crear Tablero ###

## Funciones ##
#Funcion para Crear un Cuadrado
def drawSquare(tur, tam):
   count=4
   while count > 0:
      tur.forward(tam*tb)
      tur.left(90)
      count -= 1

#Funcion Linea de Cuadrados
def drawLineSq(tur, length, col):
   tur.fillcolor(col)
   while length > 0:
      tur.begin_fill()
      drawSquare(tur, 1)
      tur.end_fill()
      tur.forward(tb)
      length -= 1

#Funcion para Crear un Triangulo
def drawTriangle(tur):
   tur.left(90)
   tur.forward(tb)
   tur.right(135)
   tur.forward(7200**(0.5))
   tur.right(90)
   tur.forward(7200**(0.5))
   tur.right(135)
   tur.forward(2*tb)

#Funcion crear 'Brazos' del tablero.
def drawArm(tur,col):
   #Primera Linea
   drawLineSq(tur, 6, 'white')
   tur.fillcolor(col)
   #Segunda Linea
   tur.left(90)
   tur.forward(2*tb)
   tur.left(90)
   drawLineSq(tur, 5, col) #Linea de Cuadros de Color
   drawSquare(tur, 1) #Cuadrado Final en Blanco
   #Tercera Linea
   tur.forward(tb)
   tur.left(180)
   drawSquare(tur, 1) #Primer Cuadro en Blanco
   tur.forward(tb)
   tur.begin_fill()
   drawSquare(tur, 1) #Segundo Cuadro de Color
   tur.end_fill()
   tur.forward(tb)
   drawLineSq(tur, 4, 'white') #Linea de Cuadros en Blanco
   #Triangulo Central
   tur.fillcolor(col)
   tur.begin_fill()
   drawTriangle(tur)
   tur.end_fill()
   #Posicionar Tortuga para Cuadrado de las Base
   tur.pu()
   tur.forward(2*tb)
   tur.left(90)
   tur.forward(6*tb)
   tur.left(180)
   tur.pd()
   #Dibujar Cuadrado de las Bases
   tur.begin_fill()
   drawSquare(drawer, 3)
   tur.end_fill()
   #Posicionar Tortuga para Siguiente Brazo
   tur.pu()
   tur.forward(6*tb)
   tur.left(90)
   tur.forward(5*tb)
   tur.right(180)
   tur.pd()

## Dibujo del Tablero ##
#Posicionar Drawer para empezar con el brazo de la derecha.
drawer.pu()
drawer.right(90)
drawer.forward(1.5*tb)
drawer.right(90)
drawer.forward(1.5*tb+6*tb)
drawer.right(180)
drawer.pd()
#Dibujar Brazos
drawArm(drawer,'red')
drawArm(drawer,'green')
drawArm(drawer,'blue')
drawArm(drawer,'yellow')
drawer.pu()
drawer.back(5*tb)
drawer.ht()

### Inicio del Juego ###

## Funciones ##
#Funcion para mover Jugadores a su Base desde el Centro del Tablero
def moveToBase(tur, rot):
   tur.right(rot)
   tur.pu()
   tur.forward(6*tb)
   tur.right(90)
   tur.forward(2*tb)
   tur.left(90)
   tur.forward(tb)
   tur.left(90)

## Desarrollo ##
#Pantalla de Bienvenida
print '---------------------------'
print '---Bienvenido a TurtLudo---'
print '---------------------------'
print ''

#Numero de Jugadores
flag = True
while flag:
   nPlayer = int(raw_input('Ingrese el numero de Jugadores [2 a 4 Jugadores]: '))
   if 2 <= nPlayer <= 4:
      flag = False
   else:
      print 'Ingrese un numero valido'
      print ''

#Creacion de las Fichas
#Jugador 1
pTito = turtle.Turtle()
pTito.shape('turtle')
pTito.color('black')
pTito.fillcolor('red')
moveToBase(pTito, 180)
#Jugador 2
pPepe = turtle.Turtle()
pPepe.shape('circle')
pPepe.color('black')
pPepe.fillcolor('blue')
moveToBase(pPepe, 0)
if nPlayer >=3:
   #Jugador 3
   pPepito = turtle.Turtle()
   pPepito.shape('square')
   pPepito.color('black')
   pPepito.fillcolor('yellow')
   moveToBase(pPepito, 90)
   if nPlayer >= 4:
      #Jugador 4
      pRodomiro = turtle.Turtle()
      pRodomiro.shape('triangle')
      pRodomiro.color('black')
      pRodomiro.fillcolor('green')
      moveToBase(pRodomiro, 270)

Ganar = False #Definir que el Juego aun no se ha ganado
turno = pTito #Definir el Turno como el del Primer Jugador

### Durante el Juego ###

## Funciones ##
#Revisa la Posicion (Redondeada) de tur para comprobar si esta en la posicion x,y.
def roundPos(tur, x, y):
   if round(tur.xcor())== round(x) and round(tur.ycor())== round(y):
      return True
   return False

#Funcion para definir el nombre de cada Jugador
def namePlayer(tur):
   if tur == pTito:
      return "Jugador 1"
   elif tur == pPepe:
      return "Jugador 2"
   elif tur == pPepito:
      return "Jugador 3"
   elif tur == pRodomiro:
      return "Jugador 4"

#Funcion para Girar la tortuga en las Esquinas
def checkEsquina(tur):
   #Cada ficha no girara en su Primera Esquina
   if tur == pTito and roundPos(tur,-7*tb,tb):
      return 0
   if tur == pPepe and roundPos(tur,7*tb,-tb):
      return 0
   if nPlayer >= 3 and tur == pPepito and roundPos(tur,-tb,-7*tb):
      return 0
   if nPlayer == 4 and tur == pRodomiro and roundPos(tur,tb,7*tb):
      return 0
   #Esquinas Generales
   if roundPos(tur,-7*tb,tb) or roundPos(tur,-7*tb,-tb) or roundPos(tur,-tb,-7*tb) or roundPos(tur,tb,-7*tb) or roundPos(tur,7*tb,-tb) or roundPos(tur,7*tb,tb) or roundPos(tur,tb,7*tb) or roundPos(tur,-tb,7*tb):
      tur.left(90)
   if roundPos(tur,tb,tb) or roundPos(tur,tb,-tb) or roundPos(tur,-tb,tb) or roundPos(tur,-tb,-tb):
      tur.right(90)
   #Girar Tortuga hacia la Recta Final
   if tur == pTito:
      if roundPos(tur, -6*tb,tb):
         tur.left(90)
      if roundPos(tur, -6*tb,0):
         tur.seth(0)
   if tur == pPepe:
      if roundPos(tur, 6*tb,-tb):
         tur.left(90)
      if roundPos(tur, 6*tb,0):
         tur.seth(180)
   if nPlayer >= 3 and tur == pPepito:
      if roundPos(tur, -tb,-6*tb):
         tur.left(90)
      if roundPos(tur, 0,-6*tb):
         tur.seth(90)
   if nPlayer == 4 and tur == pRodomiro:
      if roundPos(tur, tb,6*tb):
         tur.left(90)
      if roundPos(tur, 0,6*tb):
         tur.seth(270)

#Funcion para detectar Tope entre dos Fichas
def topeFichas(tur, tur2):
   if roundPos(tur,tur2.xcor(),tur2.ycor()):
      return True
   else:
      return False

#Funcion para mover cada tortuga a su Base
def tpBase(tur):
   if tur == pTito:
      tur.goto(-7*tb,2*tb)
      tur.seth(270)
   elif tur == pPepe:
      tur.goto(7*tb,-2*tb)
      tur.seth(90)
   elif tur == pPepito:
      tur.goto(-2*tb,-7*tb)
      tur.seth(0)
   elif tur == pRodomiro:
      tur.goto(2*tb,7*tb)
      tur.seth(180)

#Funcion para "Comer" una ficha si tur esta sobre tur2
def checkComer(tur,tur2):
   if topeFichas(tur,tur2):
      tpBase(tur2)

#Funcion General para "Comer" una ficha al pasar sobre ella, siendo tur la tortuga que "come".
def comer(tur):
   if tur == pTito:
      checkComer(tur,pPepe)
   if tur == pPepe:
      checkComer(tur,pTito)
   if nPlayer >= 3:
      if tur == pTito:
         checkComer(tur,pPepito)
      if tur == pPepe:
         checkComer(tur,pPepito)
      if tur == pPepito:
         checkComer(tur,pTito)
         checkComer(tur,pPepe)
   if nPlayer == 4:
      if tur == pTito:
         checkComer(tur,pRodomiro)
      if tur == pPepe:
         checkComer(tur,pRodomiro)
      if tur == pPepito:
         checkComer(tur,pRodomiro)
      if tur == pRodomiro:
         checkComer(tur,pTito)
         checkComer(tur,pPepe)
         checkComer(tur,pPepito)

#Funcion para detectar si la Tortuga esta en el final
def inTheEnd(tur):
   if tur == pTito and roundPos(tur,-tb,0):
      return True
   if tur == pPepe and roundPos(tur,tb,0):
      return True
   if nPlayer >= 3 and tur == pPepito and roundPos(tur,0,-tb):
      return True
   if nPlayer == 4 and tur == pRodomiro and roundPos(tur,0,tb):
      return True
   return False

#Funcion que define que pasara en cada Turno
def turno(tur):
   dado = 6 #Permite que el Loop se ejecute por primera vez
   while dado == 6: #Se repetira el turno cuando el dado sea igual a 6
      adel=True #Define que la Tortuga avanzara hacia adelante
      dadStr = " "
      while dadStr != "l":
         dadStr = raw_input(namePlayer(tur) + ": Presione l para lanzar el dado: ")
      dado = random.randint(1,6)
      print "El", namePlayer(tur), "obtuvo un", dado, "en el dado... moviendo ficha."
      count = dado
      while count > 0: #La ficha se movera hasta que el contador sea 0
         if inTheEnd(tur):
            adel=False #Si la tortuga llega al final, la tortuga ahora avanzara hacia atras
         if adel:
            checkEsquina(tur)
            tur.forward(tb)
         else:
            tur.back(tb)
         count -= 1
      comer(tur)
      if inTheEnd(tur):
         return True
   print ""
   if inTheEnd(tur):
      return True
   else:
      return False

## Desarrollo ##
while Ganar == False:
   Jug = pTito
   if Jug == pTito:
      if turno(Jug):
         break
      Jug = pPepe
   if Jug == pPepe:
      if turno(Jug):
         break
   if nPlayer >= 3:
      Jug = pPepito
      if turno(Jug):
         break
      if nPlayer == 4:
         Jug = pRodomiro
         if turno(Jug):
            break

print ""
print "FIN DEL JUEGO!!"
print ""
print "El ganador es el", namePlayer(Jug)
raw_input()
