#Hoja de trabajo 3

#Ejercicio 1
key = input("Introduzca una contraseña: ")
password = input("Introduzca su contraseña: ")
if key == password:
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta")

#Ejercicio 2
name = input("¿Cuál es tu nombre? ")
gender = input("¿Eres hombre o mujer? (Introduce H o M): ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)