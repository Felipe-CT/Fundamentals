# Bloque 1
from turtle import end_fill


x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1-Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15

# 2-Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
directorio_deportes['basketball'][1]='Bryant'

# 3-En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0]="Andrés"

# 4-Cambia el valor 20 en z a 30.
z[0]['y']=30


"""
Bloque 2
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
Por ejemplo, dada la siguiente lista:

"""

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for key in some_list:
        print(key)

"""
Bloque 3
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, 
iterateDictionary2('name', estudiantes) debería generar:
"""
def iterateDictionary2(key_name,some_list):
    x=0
    for key in some_list:
        print(some_list[x][key_name])
        x+=1
"""
Bloque 4
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
asociados dentro de la lista de cada clave. Por ejemplo:
"""
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_list):
    for key in some_list:
        print(str(len(some_list[key]))+' ' + key)
        for x in range(len(some_list[key])):
            print(some_list[key][x])
        print()
