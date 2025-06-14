# Listas vacías las cuales serán completadas
dniA_list = []
dniB_list = []

def TransformarLista(element, target_list): # Pasamos los datos ingresados por el usuario(string) a una lista.
    for e in element:
        target_list.append(e) # Recorremos un string e incluimos esos elementos iterados en la lista objetivo

def ListaFiltrada(original_list): # Esta función filtra los números repetidos para cumplir con la regla de los conjuntos (Los elemenos no deben repetirse dentro de un conjunto)
    filtered = [] # Lista donde colocaremos los elementos únicos
    filtered.append(original_list[0]) # Sumamos sólo el primer elemento de la lista 
    for i in original_list:
        if i not in filtered: # Preguntamos si el elemento de la lista original se encuentra dentro de la lista filtrada, si no es así lo incluimos
            filtered.append(i)

    return filtered # La función retorna la lista filtrada con los elementos únicos, es decir, cumple la condición de ser llamada un "conjunto"

def InsertData(subject):
    user_input = input(f"Ingrese el número de DNI del sujeto {subject}: ") # El usuario ingresa los datos

    return user_input

# La función TranformacionDeDatos nos retorna una lista filtrada, cumpliendo las condiciones de un conjunto
def TransformacionDeDatos(target_list, empty_list):
    TransformarLista(target_list, empty_list) # Tranforma los datos de tipo string ingresados por el usuario a una lista con elementos repetidos
    empty_list = ListaFiltrada(empty_list) # Se filtra la lista a elementos únicos dentro de la variable empty_list

    return empty_list # Retorna las listra filtrada cumpliendo las condiciones de un conjunto

# Inicio del programa

dniA = InsertData('A')
dniB = InsertData('B')

dniA_list = TransformacionDeDatos(dniA, dniA_list)
dniB_list = TransformacionDeDatos(dniB, dniB_list)

allNumbers = dniA_list + dniB_list

# Operación Union ( A U B )
def Union():
    filtered = []
    filtered.append(allNumbers[0])
    for i in allNumbers:
        if i not in filtered:
            filtered.append(i)

    return filtered

union_list = Union() # Guardo el retorno de la función Union para utilizarla más tarde

# Operación Interseccion ( A ∩ B )
def Interseccion(): # Se utiliza una lista filtrada para guardar elementos que se encuentran tanto en la lista A como en B
    filtered = [] # Lista filtrada
    for e in union_list: # Recorremos el retorno de la funcion Union porque contiene elementos únicos y nos sirve para utilizarlos en la comparación
        if e in dniA_list and e in dniB_list: # Preguntamos si el elemento se encuentra en ambas listas (A y B). Acá es donde realizamos la comparación
            filtered.append(e) # Añadimos el elemento que se encuentra en ambas listas en la lista filtered
    return filtered

# Operación diferencia ( x - y )
def Diferencia(x, y):
    filtered = x.copy() # Usamos el método copy para copias los valores de la variable x(que será una lista) en la variable filtered. Si no utilizamos el método copy, estaríamos pasando las variables por referencia
    for e in x: # Recorremos la lista o conjunto que se usará como el minuendo 
        if e in y: # Preguntamos si el elemento se encuentra dentro del otro conjunto utilizado como sustraendo
            filtered.remove(e) # Se remueve el valor que está dentro de la lista filtrada y el conjunto sustraendo
    return filtered # Se retorna la lista filtrada con la diferecia x - y

# Operación diferencia simétrica
def DiferenciaSimetrica(target_list,x, y):
    filtered = target_list.copy()
    for e in union_list:
        if e in x and e in y:
            filtered.remove(e)
    return filtered

# Conteo de frecuencia
def FrequencyCounter(target_list):
    frequency = {} # Contruímos un diccionario vacío donde irán anotadas la frecuencias de cada número en un formato clave:valor.
    for e in target_list: # La variable target_list contiene una lista a analizar
        frequency[e] = target_list.count(e) # El método count nos devuelve el número de coincidencias dentro de una lista dentro de una variable que pasemos como parámetro
    return frequency # Se retorna el diccionario con la información de los números de coincidencias en la lista objetivo

# Suma total de los digitos de cada DNI
def SumDigits(target_list):
    sum = 0
    for e in target_list:
        sum += int(e) # Sumamos los digitos de la lista objetivo a la variable sum para luego retornarla con todos sus elementos sumados
    return sum

# La siguiente sección del código muestra evaluaciones lógicas vinculadas con las expresiones escritas
# En esta sección voy a usar sets para diversificar un poco el código
setA = {4, 3, 5, 8, 2, 0} # Definimos el conjunto A
setB = {2, 8, 4, 1, 5} # Definimos el conjunto B

# "Los digitos que están en B y no están en A"
def LogicalEvaluation1(a, b):
    difference = a - b # Le restamos al conjunto A el conjunto B
    return difference

# "Los digitos que están en A y también en B"
def LogicalEvaluation2(a, b):
    intersection = a & b # Realizamos una intersección de dos conjuntos
    return intersection

# "Los digitos que están en A y también en B pero no en ambos"
def LogicalEvaluation3(a, b):
    diff = a ^ b # Acá estariamos realizando una diferencia simétrica entre conjuntos
    return diff

# Resultados

# Las siguientes líneas de código corresponden a: la generación automática de los conjuntos de dígitos únicos,
# conteo de frecuencia de cada dígito en cada DNI, suma total de los dígitos de cada DNI

print("#### Generación de conjuntos ####")

print(f"Generación automática de conjuntos, A = {dniA_list}") # Ambas líneas nos muestran la generación automática de conjuntos utilizando estructuras repetitivas. Esta línea en particular muestra el conjunto A
print(f"Generación automática de conjuntos, B = {dniB_list}") # y esta otra línea nos muestra el conjunto B
print(f"Frecuencia de cada digito: {FrequencyCounter(dniB)}") # Muestra la frecuencia de números presentes en un conjunto
print(f"Suma total de los digitos de cada DNI: {SumDigits(dniA_list)}") # Mostramos la suma total de el conjunto A

print("#### Evaluación de operaciónes entre conjuntos ####")

# Las siguientes líneas de código corresponden al cálculo, y visualización de: unión, intersección, diferencias y diferencia simétrica
print(f"Union = {union_list}") # Muestra la unión de dos conjuntos
print(f"Intersección = {Interseccion()}") # Muestra la intersección de dos conjuntos
print(f"Diferencia ( A - B ) = {Diferencia(dniA_list, dniB_list)}") # Muestra la diferencia entre dos conjuntos (A - B)
print(f"Diferencia ( B - A ) = {Diferencia(dniB_list, dniA_list)}") # Muestra la diferencia entre dos conjuntos (B - A)
print(f"Diferencia simétrica = {DiferenciaSimetrica(union_list,dniA_list, dniB_list)}") # Muestra la diferencia simétrica entre dos conjuntos
# En el primer argumento mandamos la unión de los conjuntos para sólo consultar los elementos únicos

print("#### Evaluación de operaciones entre conjuntos vinculadas con expresiones ####")

# Resultados evaluación de condiciones lógicas
print("Las siguientes líneas muestran evaluaciones de expresiones lógicas vinculadas con las expresiones escritas")
print(f"Los digitos que están en B y no están en A = {LogicalEvaluation1(setB, setA)}")
print(f"Los digitos que están en A y también en B = {LogicalEvaluation2(setA, setB)}")
print(f"Los digitos que están en A y también en B pero no en ambos = {LogicalEvaluation3(setA, setB)}")