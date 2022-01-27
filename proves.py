x = int(input("Nombre enter 1: "))
y = int(input("Nombre enter 2: "))
if x < y:
    while x != y:
        x = x + 1
        print(x, "+ 1 =", x, ("(while x != y)"))
else:
    print("No es pot dur a terme.")