#Arnau Gràcia Taberner - 2DAM

#Exercici 1
print("Exercici 1.")
x1 = int(input("Dona'm el primer nombre: "))
x2 = int(input("Dona'm el segon nombre: "))
mitjana = (x1+x2)/2
print("Mitjana aritmètica: ", mitjana)

#Exercici 2
print("\nExercici 2.")
x1 = float(input("Dona'm una distancia en peus: "))
x2 = float(input("Dona'm una distancia en polçades: "))
x1 = (x1 * 12) * 2.54
x1 = x2 * 2.54
print("Distancia de peus a centímetres (passant per polçades): ", x1)
print("Distancia de polçaces a centímetres : ", x2)

#Exercici 3
print("\nExercici 3.")
x1 = float(input("Dona'm una temperatura en graus Celsius: "))
x1 = 1.8 * x1 + 32
print("Temperatura en graus Fahrenheit: ", x1)

#Exercici 4
print("\nExercici 4.")
x1 = int(input("Dona'm una quantitat de segons: "))
x1 = float(x1 / 60)
print("Temps en minuts i segons: ", x1)

#Exercici 5
print("\nExercici 5.")
vocals = ["a", "e", "i", "o", "u"]
print("Llista inicial: ", vocals)
print("Part a.")
n_e = int(input("Quin número de la llista vols modificar? "))
v_e = input("I amb quin valor? ")
vocals[n_e] = v_e
print("Llista modificada: ", vocals)
print("Part b.")
lletra = input("Quina lletra de la llista vols modificar? ")
v_e = input("I amb quin valor? ")
i = vocals.index(lletra)
vocals[i] = v_e
print("Llista modificada: ", vocals)   

#Exercici 6
print("\nExercici 6.")
mult = [x*7 for x in range(11)]
print("Taula de multiplicar del 7: ", mult)

#Exercici 7
print("\nExercici 7.")
d = {"Aida" : 7, "Jordi" : 8, "Toni" : 6, "Arnau" : 5}
print("Diccionari: ", d)
alumne = input("De quin alumne vols sabe la nota? ")
print("Resultat de ", alumne,  ": ", d[alumne])

#Exercici 9
print("\nExercici 9.")
x = int(input("Dona'm un nombre enter:"))
y = int(input("Dona'm un segon nombre enter:"))
if y != 0:
    print("Divisió: ", x / y)
else:
    print("El segon nombre enter és 0, no es pot dividir.")

#Exercici 10
print("\nExercici 10.")
import math

area = int(input("Càlcul area: Triangle(1) o cercle(2)"))
if area == 1:
    base = float(input("Dona'm la base:"))
    altura = float(input("Dona'm l'altura:"))
    print("Area triangle: ", (base*altura)/2)
elif area == 2:
    radi = float(input("Dona'm el radi:"))
    print("Area cercle: ", math.pi*(radi**2))
else:
    print("No has seleccionat cap, good bye")

#Exercici 13
print("\nExercici 13.")
x = int(input("Nombre enter 1: "))
y = int(input("Nombre enter 2: "))
if x < y:
    while x != y:
        x = x + 1
        print(x, "+ 1 =", x, ("(while x != y)"))
else:
    print("No es pot dur a terme.")

#Exercici 14
print("\nExercici 14.")
from math import factorial
n = int(input("Dona'm un nombre enter: "))
if n > 0:
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
print(factorial)

#Exercici 15
print("\nExercici 15.")
for i in range(1,100):
    if i % 7 == 0:
        print(i)

#Exercici 24
print("\nExercici 24.")
mD = []
for n in range(1,11):
    mD.append(2*n)
print(mD)

#Exercici 25
print("\nExercici 25.")
mD = []
n = int(input("n: "))
m = int(input("m: "))

for x in range(1,x + 1):
    mD.append(m*x)
print(mD)


#Exercici 26
print("\nExercici 26.")
enter = input("Enter a word: ")
ordered = sorted(enter)
enter = list(enter)
if ordered == enter:
    print("This is an alphabetic word")
else:
    print("This is not an alphabetic word")

#Exercici 27
print("\nExercici 27.")
enter = input("Introdueix una paraula: ")
eneter = list(enter)
enter.remove(' ')
auxiliar = enter
enter.reverse()
if enter == auxiliar:
    print("Palíndroma")
else:
    print("No palíndroma")


#Exercici 29
print("\nExercici 29.")
words = []
x = ""
with open ("paraules.txt") as file:
    for line in file:
        words = line.strip().split(' ')
        for word in words:
            if word.upper() not in map(str.upper, words):
                words.append(word)
print (sorted(words))