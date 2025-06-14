from itertools import product

# Inicializamos las variables en 0
yearA = 0
yearB = 0

# Definimos una constante la cual será el año actual
CURRENT_YEAR = 2025

# Pedimos por consola los años de nacimiento de dos usuarios
yearA = int(input("Ingresa el año de nacimiento de A: "))
yearB = int(input("Ingresa el año de nacimiento de B: "))

# Creamos una lista con las variables ingresadas por el usuario
usersYearList = [yearA, yearB]

# Calcular cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
def CalculatePairYear(target_list):
    counterPair = 0 # Inicializamos un contador que nos indica la cantidad de años pares en la lista
    for e in target_list:
        if e % 2 == 0: # Verificamos que el residuo sea 0
            print(f"El año {e} es un año par")
            counterPair += 1 # Si el año es par sumamos una unidad al contador
        else:
            print(f"El año {e} no es un año par")
    return counterPair # Retornamos la cantidad de veces que se ha encontrado un año par en la lista

# Calcular si el año es bisiesto
# Para calcular el año bisiesto tenemos en cuenta que el número debe ser divisible entre 4
# excepto si también es divisible entre 100, al menos que también sea divisble entre 400
def CalculateLeapYear(year):
    if year % 4 == 0 and ( not year % 100 == 0 or year % 400 == 0 ):
        print(f"{year}!! Tenemos un año especial.") # Tenemos un año bisiesto
    else:
        print(f"El año {year} es un año bisiesto") # El año no es bisiesto

# Obtenemos un set del año de nacimiento de cada usuario
def GetSetOfBirthYear(target_list): 
    currentUsersYears = set() # Inicializamos un set para almacenar los años de nacimiento de los usuarios

    for e in target_list:
        currentUsersYears.add(e) # Añadimos los años de nacimiento extraídos de la lista al set previamente creado

    return currentUsersYears # Retornamos el set

# Obtenemos un set de la edad actual de cada usuario
def GetSetOfCurrentUserYears(target_list):
    current_user_year_set = set() # Inicializamos un set para las edades actuales de los usuarios

    for e in target_list:
        current_user_year_set.add(CURRENT_YEAR - e) # Restamos el año actual con el año de nacimiento de cada usuario para obtener su edad actual

    return current_user_year_set # Retornamos el set de edades de los usuarios

def CalculateCartesianProduct(setA, setB):
    return list(product(setA, setB)) # Utilizamos los métodos list y product para obtener y retornar el producto cartesiano de años de nacimiento y edades

# Resultados
print("#### Calcular años pares ####")
print(f"Se han detectado {CalculatePairYear(usersYearList)} año(s) pares entre los usuarios")
print("#### Calcular año bisiesto ####")
CalculateLeapYear(yearA)
print("#### Calcular producto cartesiano entre años y edades actuales ####")
print(CalculateCartesianProduct(GetSetOfBirthYear(usersYearList), GetSetOfCurrentUserYears(usersYearList)))
