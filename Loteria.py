import random
numeros = []

x = int(input(""" --------------------RECOMENDACIONES -----------------------------------------
Mientras mayor sea la cantidad de valores, mayor sera el premio, pero menor la posibilidad de ganar el premio
Introduzca la cantidad de números a jugar: """))
if x <= 0:
    print("Escoja un numero del 1 en adelante")
    exit()
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    while len(numeros) < x:
        valor = int(input("introduzca un número: "))
        if valor > 99:
            print("Ingrese un número entre 0-99")
        else:
            numeros.append(valor)
else:
    resta = 18 - edad
    print(f"Vuelva en {resta} años, gracias por su participación")
    exit()

numeros_aleatorios = [random.randint(0, 99) for _ in range(x)] 

print(f"Los números que usted escogio: {numeros}")
print(f"Los números ganadores son: {numeros_aleatorios}")

if 1 <= x <= 2 and numeros_aleatorios == numeros:
    print('Haz ganado 10,000 de dólares')
elif 3 <= x <= 5 and numeros_aleatorios == numeros:
    print('Haz ganado 100,000 de dólares')
elif 6 <= x <= 10 and numeros_aleatorios == numeros:
    print('Haz ganado 1MM de dólares')
elif 11 <= x <= 15 and numeros_aleatorios == numeros:
    print('Haz ganado 1,000MM de dólares')
elif 15 <= x <= 20 and numeros_aleatorios == numeros:
    print('Haz ganado 1BB de dólares')
elif 21 <= x <= 100 and numeros_aleatorios == numeros:
    print('Haz ganado 1000BB de dólares')
else:
    print("Ha desperdiciado su tiempo, nunca juegue a loteria")