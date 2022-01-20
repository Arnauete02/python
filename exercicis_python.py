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