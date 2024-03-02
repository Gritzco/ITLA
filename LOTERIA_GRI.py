import random
Loteria = []

while len(Loteria) < 10: 
    nombre = input("Ingresa un nombre: ")
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        Loteria.append(nombre)
    else:
        resta = 18 - edad
        print(f"Vuelva en {resta} años, gracias por su participación")

print("Los nombres ingresados son:")
for nombre in Loteria:
    print(nombre)

print()
print()
print()
print()
print("OJO SE MUESTRAN LOS NOMBRES ESCRITOS PARA QUE HAYA TRANSPARENCIA")

print()
print()
print()
print()

GANADOR = random.choice(Loteria)
print(f"el ganador es: {GANADOR}")