"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

"""user=input('escriba una palabra: ' )
for i in range(0,10):
    print(user)"""

"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

"""edad=int(input('inserte su edad: '))
for i in range(1,edad+1):
    print(i)"""

"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

"""num=int(input('inserte un numero entero positivo: '))

for i in range(1,num+1,2):
    print(i,end=',')"""

"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

"""num=int(input('inserte un numero entero positivo: '))

for i in range(num,-1,-1):
    print(i,end=',')"""

"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

"""inv=float(input('inserte el monto a invertir: '))
inte=float(input('inserte el interes anual: '))
ano=int(input('inserte la cantidad de años: '))

saldo=inv

for i in range(ano):
    inv *= 1 + inte / 100
    print('El saldo total es de ' + str(inv) + '. La ganancia en el año ' + str(i+1) + ' es de ' + str(inv - saldo) + '.')"""

"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****"""

"""num=int(input('inserte un numero: '))

for i in range(num):
    print('*'*(i+1))"""

"""Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

"""for i in range(1,11):
    print(i*10)"""

"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""

"""n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")"""

"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

"""contrase='Albatroz'

while contrase!=input('inserte la contraseña:'):
    continue"""

"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

"""num=int(input('inserte un numero enter: '))
primo='Si'

for i in range(2,num):
    if num%i==0:
        primo='No'

print(f'el numero {num} {primo} es primo')"""

"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última."""

"""palabra=input('inserte una palabra: ')

for i in range(-1,-len(palabra)-1,-1):
    print(palabra[i])"""


"""Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""

"""frase=input('inserte una frase: ')
letra=input('inserte una letra: ').lower()

cont=0

for i in frase:
    if i ==letra:
        cont+=1

print(f'la frase contiene {cont} {letra}')"""

"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""

"""entra=input('inserte: ')

while entra!='salir':
    print(f'ECO {entra}')
    entra=input('inserte: ')"""