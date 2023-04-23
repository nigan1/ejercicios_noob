"""Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

"""edad=int(input('inserte su edad'))

if edad>17:
    print('eres mayor de edad')
else:
    print('eres menor de edad')"""

"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

"""contra='almacenSito'
passw=input('inserte su contraseña: ')

if contra.lower()==passw.lower():
    print('la contraseña coincide')
else:
    print('contraseña incorrecta')"""

"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error."""

"""num1=float(input('inserte el primer numero: '))
num2=float(input('inserte el segundo numero: '))

if num2==0:
    print('no se puede dividir por 0')
else:
    print(num1/num2)"""

"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

"""numero=int(input('inserte un numero entero: '))

if numero%2==0:
    print('el numero es par')
else:
    print('es impar')"""

"""Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

"""edad=int(input('inserte su edad: '))
ingresos=float(input('inserte sus ingresos mensuales: '))

if edad>16 and ingresos>=1000:
    print('tiene que tributar')
else:
    print('no tiene que tributar')"""

"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

"""nombre=input('inserte su nombre: ')
sexo=input('inserte su sexo M o F: ').lower()

if sexo=='f' and nombre[0]<'m' or sexo=='m' and nombre[0]>'n':
    print('pertenece al grupo A')
else:
    print('pertenece al grupo B')"""

"""Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	               Tipo impositivo

Menos de 10000€             5%
Entre 10000€ y 20000€	   15%
Entre 20000€ y 35000€	   20%
Entre 35000€ y 60000€	   30%
Más de 60000€	           45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
"""renta=float(input('inserte su renta anual: '))

if renta<1000:
    print('5 ')
elif renta<20000:
    print('15 ')
elif renta<35000:
    print('20 ')
elif renta<60000:
    print('30 ')
else:
    print('45 ')"""


"""Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario."""

"""puntuacion=float(input('inserte la puntuacion obtenida: '))
dinero=2400

if puntuacion==0.0:
    print(f'Su nivel es inaceptable, por lo que cobrara {puntuacion*dinero}')
elif puntuacion==0.4:
    print(f'Su nivel es aceptable, por lo que cobrara {puntuacion*dinero}')
elif puntuacion>=0.6:
    print(f'Su nivel es meritorio, por lo que cobrara {puntuacion*dinero}')"""

"""Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""


"""edad=int(input('digite su edad: '))

if edad<4:
    print('Su entrada es gratis!!')
elif edad<=18:
    print('Su entrada cuesta 5 euros!!')
elif edad>18:
    print('Su entrada cuesta 10 euros!!')
else:
    print('edad incorrecta')"""

"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

pizza=input('desea una pizza vegetariana? S/N: ')

print('la mozzarella y el tomate que están en todas la pizzas')

if pizza.lower()=='s':
    ingrediente=input('si desea agregar Pimiento digite 1, si desea Tofu presione 2: ')
    if ingrediente==1:
        print('La pizza elegida e vegetariana con ingredientes mozzarella,tomate y tofu')
    else:
        print('La pizza elegida e vegetariana con ingredientes mozzarella,tomate y pimiento')
else:
    ingrediente=input('si desea agregar Peperoni digite 1, si desea Jamón presione 2 o si desea Salmón digite 3: ')
    if ingrediente==1:
        print('La pizza elegida no es vegetariana contiene los ingredientes mozzarella,tomate y Peperoni')
    elif ingrediente==2:
        print('La pizza elegida no es vegetariana contiene los ingredientes mozzarella,tomate y Jamón')
    else:
        print('La pizza elegida no es vegetariana contiene los ingredientes mozzarella,tomate y Salmón')