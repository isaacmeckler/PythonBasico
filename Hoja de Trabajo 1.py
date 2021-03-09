#Hoja de trabajo 1

# Ejercicio 1
n = int(input("Introduce un número entero postivo: "))
for i in range(n+1):
    print("*"*i)

# Ejercicio 2
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")


# Ejercicio 3
n = int(input("Introduce un número entero positivo: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es un número primo")
else: 
    print(str(n) + " no es un número primo")