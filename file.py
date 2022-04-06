num1 = 42   # variable declaration, number
num2 = 2.3  # variable declaration, number
boolean = True  # variable declaration, bolean 
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # tuple declaration, string
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary declaration, string, number, boolean
fruit = ('blueberry', 'strawberry', 'banana') # tuple declaration
print(type(fruit))  # comando que entrega por consola el tipo de objeto que es 'fruit', tuple
print(pizza_toppings[1]) # comando que entrega por consola el objeto en la posicion [1] de la tupla 'pizza_toppings' el cual es 'Sausage'
pizza_toppings.append('Mushrooms') # comando que agrega el objeto 'Mushrooms' a la tupla pizza_toppings, el objeto se agregara como susesor de la ultima posicion de la tupla
print(person['name']) # comando que imprime por pantalla el objeto ingresado como 'name' en el diccionario 'person', se imprime en pantalla 'John'
person['name'] = 'George' # comando que actualiza el valor del objeto ingresado como 'name' a 'George' 
person['eye_color'] = 'blue' # comando que agrega el el objeto 'eye_color' y le asigna el calor 'blue'
print(fruit[2]) # comando que entrega por consola el objeto en la posicion [2] de la tupla 'fruit' el cual es 'banana'

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
"""
comando if, condicionante que evalua el valor de 'num1' y lo compara bajo el criterio
'mayor que' frente al valor de control declarado como '45', en caso de que dicha comparacion
sea verdadera, se mostrara por consola la declaracion "It's greater", en caso de ser falsa
se mostrara la declaracion "It's lower".
para este caso la declaracion se considera falsa, ya que 'num1 = 42' y se mostrara por pantalla 
"It's lower"
"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
"""
comando if, condicionante que evalua la cantidad de caracteres en la variable 
'string', lo compara bajo el criterio 'menor que' frente al valor de control 
declarado como '5', en caso de que esta declaracion se considere verdadera, se 
mostrara por consola "It's a short word!", de lo contrario se ejecutara el 
comando elif, el cual evalua como condicionante la cantidad de caracteres en la 
variable 'string', lo compara bajo el criterio 'mayor que' frente al valor de 
control declarado como '15', en caso de que esta declaracion se considere verdadera
se mostrara por consola "It's a long word!".
En caso de que el comando if y elif se consideren falsas, se ejecutara el comando el
else, el cual imprime por consola "Just right!"

Para este caso en particular, se mostrara por consola "Just right!"
"""

for x in range(5):
    print(x)
"""
el comando for evaluara el valor de x, mientras este se mantenga en un rango declarado 
ejecutara las indicaciones declaradas en su interior, para este caso x sera evaluado 
bajo el criterio de range, en el cual se declaran los valores de inicio, termino y el
criterio de iteracion, para este caso se declara solo el valor de termino '5', por lo que
se considera como valor de inicio el '0' y el criterio de itereacion '1'.
el comando print, dentro del comando for, mostrara por pantalla por pantalla todos los 
valores de x mientras el criterio de evaluacion for se mantenga como verdadero.
se mostraran por pantalla los valores:
0
1
2
3
4
"""


for x in range(2,5):
    print(x)
"""
el comando for evaluara el valor de x, mientras este se mantenga en un rango declarado 
ejecutara las indicaciones declaradas en su interior, para este caso x sera evaluado 
bajo el criterio de range, en el cual se declaran los valores de inicio, termino y el
criterio de iteracion, para este caso se declara solo el valor de inicio '2' y el 
valor de termino '5',no se entrega criterio de iteracion, por lo que se considera 
como '1'.el comando print, dentro del comando for, mostrara por pantalla por pantalla 
todos los valores de x mientras el criterio de evaluacion for se mantenga como 
verdadero.
se mostraran por pantalla los valores:
2
3
4
"""
for x in range(2,10,3):
    print(x)
"""
el comando for evaluara el valor de x, mientras este se mantenga en un rango declarado 
ejecutara las indicaciones declaradas en su interior, para este caso x sera evaluado 
bajo el criterio de range, en el cual se declaran los valores de inicio, termino y el
criterio de iteracion, para este caso se declara solo el valor de inicio '2', el 
valor de termino '10' y como criterio de itereacion '3'.
el comando print, dentro del comando for, mostrara por pantalla por pantalla todos 
los valores de x mientras el criterio de evaluacion for se mantenga como verdadero.
se mostraran por pantalla los valores:
2
5
8
"""

x = 0
while(x < 5):
    print(x)
    x += 1
"""
se declara 'x' con un valor de '0'.
el comando while ejecutara las indicaciones declaradas en su interior mientras el 
enunciado entre parentesis se mantenga como verdadero.
las indicaciones incluyen mostrar por consola el valor de 'x' y posterior a esto 
adicionara '1' al valor de 'x', finalmente volvera a reiniciar el ciclo while
para este caso, se mostrara por consola
0
1
2
3
4
"""

pizza_toppings.pop()
pizza_toppings.pop(1)
"""
comando pop elimina un objeto de la tuple, cuando es usado sin indicar el objeto 
a eliminar, se elimina el objeto en la ultima posicion, en este caso se eliminan:
'Mushrooms'
'Sausage'
"""

print(person) #se imprime por consola el directorio completo
person.pop('eye_color') #se elimina del directorio la categoria 'eye_color'
print(person) #se imprime por consola el directorio completo

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
"""
la estructura de este comando recorre la tuple 'pizza_topings', si encuentra el elemento
'Pepperoni' mostrara por consola 'After 1st if statement', posterior a eso evaluara el
siguiente elemento, si este elemento es 'Olives', el ciclo for terminara.
Para este caso particular se mostrara por consola:
'After 1st if statement'
'After 1st if statement'
'After 1st if statement'
"""

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
print_hello_ten_times()
"""
se define la funcion 'print_hello_ten_times()' la cual ejecuta un ciclo for, desde '0'
hasta '10', en cada periodo se mostrara por pantalla la palabra 'Hello'.
se ejecuta la funcion 'print_hello_ten_times()', por la forma en la que ha sido definida,
la funcion no necesita valores en entrada, por lo que se puede ejecutar sin ingresar un
valor a la funcion
para este caso se mostrara por pantalla:
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
"""

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
print_hello_x_times(4)
"""
se define la funcion 'print_hello_x_times(x)' la cual ejecuta un ciclo for, desde '0'
hasta 'x', en cada periodo se mostrara por pantalla la palabra 'Hello'.
se ejecuta la funcion 'print_hello_x_times(4)', por la forma en la que se ha definido 
la funcion, es necesario entregar un valor para que la funcion se ejecute correctamente.
para este caso se mostrara por pantalla:
'Hello'
'Hello'
'Hello'
'Hello'
"""

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
"""
se define la funcion 'print_hello_x_or_ten_times(x = 10)' la cual ejecuta un ciclo 
for, desde '0' hasta 'x', dando un valor predeterminado como 'x=10' en cada periodo 
se mostrara por pantalla la palabra 'Hello'.
se ejecuta la funcion 'print_hello_x_or_ten_times()',
para este caso se mostrara por pantalla:
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
'Hello'
se ejecuta la funcion 'print_hello_x_or_ten_times(4)',
para este caso se mostrara por pantalla:
'Hello'
'Hello'
'Hello'
'Hello'
"""

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
# print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)