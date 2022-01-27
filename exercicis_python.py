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

#Exercici 8
print("\nExercici 8.")

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

#Exercici 11
print("\nExercici 11.")

#Exercici 12
print("\nExercici 12.")

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

#Exercici 15
print("\nExercici 15.")

#Exercici 16
print("\nExercici 16.")

#Exercici 17
print("\nExercici 17.")

#Exercici 18
print("\nExercici 18.")

#Exercici 19
print("\nExercici 19.")

#Exercici 20
print("\nExercici 20.")

#Exercici 21
print("\nExercici 21.")

#Exercici 22
print("\nExercici 22.")

#Exercici 23
print("\nExercici 23.")