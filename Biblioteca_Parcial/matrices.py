from Biblioteca_Parcial.validaciones import *

#--------------- busqueda ---------------#
def buscar(texto:str, lista:list):
    dato = int(input(texto))
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

#--------------- inicializar ---------------#
def menu(opciones):
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(opciones)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")
    opcion_elegida = input("elija una opcion: ")
    validar_opcion(opcion_elegida)
    while validar_opcion(opcion_elegida) == True:
        opcion_elegida = input("Error. elija una opcion correcta: ")
    return int(opcion_elegida)

def iniciar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    #esta funcion tiene la tarea de crear una matriz vacía
    #recibe cant_filas, cant_columnas y un valor con el cual rellenar
    #retornará una matriz
    matriz= []
    for i in range(cant_filas):
        i = [valor_inicial] * cant_columnas
        matriz += [i]
    return matriz
#--------------- calculos ---------------# 
def sacar_promedio(lista_numeros:list) -> float:
    acumulador = 0
    contador = 0
    for i in lista_numeros:
        acumulador += i
        contador += 1
    resultado = acumulador / contador
    return resultado

def sacar_promedio_matriz(matriz_numeros:list) -> list:
    cant_columnas = 0
    for fila in matriz_numeros:
        if len(fila) > cant_columnas:
            cant_columnas = len(fila)

    acumulador_columnas = [0] * cant_columnas
    contador_columnas = [0] * cant_columnas

    for fila in matriz_numeros:
        for i in range(len(fila)):
            acumulador_columnas[i] += fila[i]
            contador_columnas[i] += 1
    
    promedios = [0] * cant_columnas
    for i in range(cant_columnas):
        promedios[i] = acumulador_columnas[i] / contador_columnas[i]
    return promedios

def cantidad_notas_materias(notas: list, materia:int) -> list:
    contador = [0] * 10
    for i in range(len(notas)):
        contador[notas[i][materia]-1] += 1
        return contador
    
def repeticiones_notas(matriz_notas:list):
    materia = 0
    while materia <= 5:
        resultado = cantidad_notas_materias(matriz_notas, materia -1)
        print(f"recuento de notas para MATERIA{materia +1}")

        nota = 0
        while nota < 10:
            print(f"nota {nota+1}: {resultado[nota]} repeticiones")
            nota = nota + 1
        print("")
        materia = materia + 1
#--------------- carga de datos ---------------#
def cargar_promedio(lista_notas: list, lista_prom: list):
    for i in lista_notas:
        lista_prom += [sacar_promedio(i)]
    return lista_prom

def cargar_promedio_matriz(lista_notas: list, lista_prom: list, columna: int):
    for columna in lista_notas:
        lista_prom += [sacar_promedio_matriz(lista_notas, columna)]
    return lista_prom

def pedir_cantidad() -> int:
    cantidad = input("ingrese cantidad a cargar: ")
    while validar_numero(cantidad):
        cantidad = input("Error. ingrese cantidad valida: ")
    return int(cantidad)

def cargar_nombre() -> str:
    nombre = input("Ingresar nombre: ")
    while validar_nombre(nombre):
        nombre = input("Error. Ingresar nombre válido: ")
    return nombre

def cargar_genero() -> str:
    genero = input("Ingresar género[F | M | X]: ")
    while validar_genero(genero):
        genero = input("Error. Ingresar género válido[F | M | X]: ")
    return genero

def cargar_legajo(legajos_existentes:list) -> int:
    legajo = input("Ingresar legajo: ")
    while validar_legajo(legajo, legajos_existentes):
        legajo = input("Error. Ingresar legajo válido: ")
    return int(legajo)

def cargar_notas() -> list:
    cant_notas = 5
    notas = [0] * cant_notas
    for i in range(cant_notas):
        nota = input(f"Ingrese nota del alumno en MATERIA{i+1}: ")
        while validar_nota(nota):
            nota = input(f"Error. Ingrese una nota valida: ")
        notas[i] = int(nota)
    return notas

def cargar_datos(nombres:list, generos:list, legajos:list, notas:list, cant:int) -> None:
    for i in range(cant):
        nombres[i] = cargar_nombre()
        generos[i] = cargar_genero()
        legajos[i] = cargar_legajo(legajos)
        notas[i] = cargar_notas()
#--------------- ordenamiento ---------------#
def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list, lista_d:list) -> None:
    for i in range(0, len(lista_a)-1, 1):
        for j in range(i + 1, len(lista_a), 1):
            if lista_c[i] > lista_c[j]:
                nombre = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre
                
                genero = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = genero
                
                legajo = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = legajo
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    genero = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = genero
                
                    nombre = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre

def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list, lista_d:list) -> None:
    for i in range(0, len(lista_a)-1, 1):
        for j in range(i + 1, len(lista_a), 1):
            if lista_c[i] < lista_c[j]:
                nombre = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre
                
                genero = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = genero
                
                legajo = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = legajo
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] < lista_a[j]:
                    genero = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = genero
                
                    nombre = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre

def ordenar_promedio(promedio_materias:list):
    indices = [0, 1, 2, 3, 4]
    for i in range (4):
        for j in range ( i + 1,5):
           if promedio_materias[i] < promedio_materias[j]:

               aux= promedio_materias[i]
               promedio_materias[i]= promedio_materias[j]
               promedio_materias[j] = aux

               aux = indices[i]
               indices[i] = indices[j]
               indices[j] = aux 
    for i in range (5):
        nombre_materia = "MATERIA" + str(indices[i] + 1) 
        print (f"Materia: {nombre_materia[i]} | Promedio : {promedio_materias[i]}")

#--------------- imprimir ---------------#
def imprimir_dato(nombre:list, genero:list, legajo:list, nota: list, indice:int, promedio = None) -> None:
    i = indice
    if promedio == None:
        print(f"{nombre[i]}\t {genero[i]}\t {legajo[i]}\t", end= "")
        for n in nota[i]:
            print(f"\t{n}\t", end= "")
        print(" ")
    else:
        print(f"{nombre[i]}\t {genero[i]}\t {legajo[i]}\t", end= "")
        for n in nota[i]:
            print(f"\t{n}\t", end= "")
        print(f"\t{promedio[i]}\t")

def imprimir_datos(nombres:list, generos:list, legajos:list, notas: list, tamano:int, promedios = None) -> None:
    for i in range(tamano):
        if promedios == None:
            imprimir_dato(nombres, generos, legajos, notas, i)
        else:
            imprimir_dato(nombres, generos, legajos, notas, i, promedios)

def mostrar_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print("")

def mostrar_lista(lista:list):
    for i in lista:
        print(f"{i}\t", end= " ")
    print(" ")

def promedio_mayor  (promedios_materias: list):
    mayor= promedios_materias [0]
    posicion= 0

    for i in range (1,5):
        if promedios_materias [i] > mayor:
            mayor = promedios_materias [i]
            posicion = i
    nombre_materia= "MATERIA" + str(posicion +1)
    print(f"Materia con mayor promedio general: {nombre_materia} | Promedio: {mayor}")