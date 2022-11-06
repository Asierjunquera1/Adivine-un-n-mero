import random
numero = random.randint(0, 100)
intento = input("Ingrese un número:")
while numero != intento:
    if numero > intento:
        print("demasiado pequeño")
    else:
        print("demasiado grande")
    intento = input("ingrese otro número:")
print("has ganado")
