"""
Escriba un código Python que entregue ciertas caracterı́sticas de un número solicitado. 
Para esto, el programa deberá realizar las siguientes tareas:
Solicitar al usuario un número entero positivo perteneciente al rango [2,1000]. Su programa debe verificar esta condición. 
En caso contrario, se debe pedir otro número hasta que se cumpla la condición.
Indicar las siguientes caracterı́sticas del número solicitado:
¿Es un número par o impar?
¿Es un número primo?
¿Cuál es el conjunto de divisores del número? (Se dice que y es divisor de x si el resultado de x ÷ y es un número entero).
Una vez indicada las caracterı́sticas del número, el programa debe finalizar. Ejemplo de funcionamiento:

Ingrese un número: 6
Número par
No es un número primo
Conjunto de divisores:
1
2
3
6
"""

from ast import Return
from re import A

def primos():
    num1 = int(input("Hola, por favor ingresa un numero entero entre 2 y 1000: "))
    if num1<2:
        print("intenta con un numero mas grande")
        primos()
    elif num1>1000:
        print("intenta con un numero mas pequeño")
        primos()
    else:
        num2=num1-1
        for num2 in range(num1; ):