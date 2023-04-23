"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""

#print('¡Hola Mundo!')

"""Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego
 muestre por pantalla el contenido de la variable."""

#variable='¡Hola Mundo!'

#print(variable)

"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la
consola y después de que el usuario lo introduzca muestre por 
pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido."""

#nombre=input('Inserte su nombre: \n')
#print(f'¡Hola {nombre}!')

"""Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética."""

#resul=((3+2)/(2*5))**2
#print(resul)

"""Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde."""

#horas=float(input('Inserte la cantidad de horas trabajadas: '))
#coste=float(input('Inserte cuanto le pagan por cada hora trabajada: '))
#print(f'le corresponde una paga de {horas*coste} por las horas de trabajo')

"""Ejercicio 6
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
 primeros enteros positivos puede ser calculada de la siguiente forma
"""

#num=int(input('inserte un numero entero y positivo: '))

#sum=(num*(num+1))/2

  
#print(f'la suma desde el 1 hasta el numero del usuario es {sum}')


"""Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa 
corporal calculado redondeado con dos decimales."""

" fórmula para el IMC es el peso en kilogramos dividido por la estatura en metros cuadrados"

#peso=float(input('inserte su peso en kilogramos: '))
#estatura=float(input('inserte su estatura en metros: '))

#imc=peso/(estatura**2)
#print(f'Tu índice de masa corporal es {round(imc,2)}')

"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por 
el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

#n=int(input('inserte un numero entero: '))
#m=int(input('inserte otro numero entero: '))
#c=n//m
#r=n%m

#print(f'la {n} entre {m} da un cociente {c} y un resto {r}')

"""Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."""

#inv=float(input('inserte la inversion inicial: '))
#int=float(input('interes anual: '))
#ano=float(input('Años a invertir: '))

#capital=inv*(int/100+1)**ano
#APR
#print(f'capital obtenido en la inversión {round(capital,2)}')

"""Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de 
los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso 
total del paquete que será enviado."""

#payasos=float(input('inserta la cantidad de payasos a enviar: '))
#toy=float(input('inserta la cantidad de muñecas a enviar: '))

#pesoPayaso=112
#pesoToy=75

#print(f'el peso total del paquete es de {pesoPayaso*payasos+toy*pesoToy}g')

"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales."""


#inv=float(input('inserte el deposito: '))
#interes=4
#ano1=inv*(interes/100+1)**1
#print(f'el primero año tiene {round(ano1,2)}')
#ano2=inv*(interes/100+1)**2
#print(f'el segundo año tiene {round(ano2,2)}')
#ano3=inv*(interes/100+1)**3
#print(f'el terceer año tiene {round(ano3,2)}')

"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total."""

descuento=60 #%
barras=int(input('barras vendidas en el dia: '))
preciodesc=3.49/100*(100-descuento)

print(f'cada barra de pan tiene un costo de  3.49€, con el descuento del 60% por no ser fresca queda en {preciodesc}€, por lo que el total en venta fue de {preciodesc*barras}€')
