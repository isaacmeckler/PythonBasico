#Hoja de Trabajo 0
print("Cual es tu peso en Kilogramos?")
peso = float(input())
print("Cual es tu estatura en Metros?")
estatura = float(input())

imc = round(peso/(estatura*estatura), 2)

print("Su indice de masa corporal es", imc)