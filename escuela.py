from Biblioteca_Parcial.validaciones import *
from Biblioteca_Parcial.matrices import *

opciones = "1. Cargar alumnos\n2. Mostrar alumnos\n3. Buscar alumno\n4. Promedios mas altos\n5. Materias con mayor promedio\n6. Cantidad de notas por materia\n7. Salir"
opciones2 = "1. salir\npresione cualquier otro numero para volver"
cant_alumnos = 30
materias = ["Matematica", "Programacion", "Arq. y Sistemas Op.", "Ingles", "Metodologia de Estudio"]

legajos = [
    10345, 10012, 10278, 10456, 10123, 10089, 10567, 10234, 10045, 10412,
    10321, 10111, 10543, 10034, 10198, 10211, 10500, 10078, 10156, 10290,
    10400, 10167, 10001, 10512, 10056, 10200, 10367, 10489, 10100, 10525
]

nombres = [
    "Juan Perez", "Maria Gomez", "Lucia Martinez", "Pedro Ramirez", "Camila Torres",
    "Nicolas Sosa", "Julieta Rios", "Facundo Diaz", "Sofia Blanco", "Bruno Ibarra",
    "Valentina Vera", "Agustin Leiva", "Martina Gom", "Ramiro Ortiz", "Dana Lujan",
    "Gonzalo Ayala", "Tamara Rojas", "Leonel Castro", "Isabel Moreno", "Franco Medina",
    "Carla Acosta", "Tomas Molina", "Emilia Nuñez", "Axel Gimenez", "Cecilia Vidal",
    "Emiliano Rojas", "Florencia Paz", "Mateo Peña", "Paula Sosa", "Alex Gomez"
]

generos = [
    'M', 'F', 'F', 'M', 'F',
    'M', 'F', 'M', 'F', 'M',
    'F', 'M', 'F', 'M', 'X',
    'M', 'F', 'M', 'F', 'M',
    'F', 'M', 'F', 'M', 'F',
    'M', 'F', 'M', 'F', 'X'
]
notas = [
    [9, 6, 7, 2, 8],
    [3, 5, 10, 6, 4],
    [8, 7, 5, 9, 6],
    [10, 9, 3, 8, 7],
    [4, 6, 7, 6, 5],
    [7, 10, 4, 8, 9],
    [5, 6, 3, 9, 8],
    [8, 7, 6, 7, 10],
    [9, 4, 7, 6, 3],
    [6, 8, 9, 10, 7],
    [4, 7, 6, 3, 8],
    [5, 9, 7, 4, 6],
    [6, 10, 8, 7, 9],
    [7, 6, 5, 4, 3],
    [10, 9, 8, 6, 7],
    [5, 3, 4, 9, 6],
    [6, 7, 8, 10, 9],
    [9, 8, 7, 5, 4],
    [7, 6, 9, 8, 10],
    [4, 5, 3, 7, 6],
    [6, 9, 10, 8, 5],
    [3, 4, 5, 6, 7],
    [8, 7, 6, 5, 4],
    [10, 9, 8, 7, 6],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 6, 5],
    [6, 5, 4, 3, 2],
    [9, 8, 7, 6, 5],
    [3, 4, 6, 7, 8],
    [5, 7, 8, 9, 10]
    ]


# nombres = [""] * cant_alumnos
# generos = [""] * cant_alumnos
# legajos = [0] * cant_alumnos
# notas = iniciar_matriz(30,5,0)
promedios = []
cargar_promedio(notas, promedios)
promedios_materias = sacar_promedio_matriz(notas)


while True:
    match menu(opciones):
        case 1:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("1. Cargar alumnos")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            cargar_datos(nombres, generos, legajos, notas, cant_alumnos)
            cargar_promedio(notas, promedios)
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    continue
        case 2:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("2. Mostrar alumnos")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            if legajos == ([0] *cant_alumnos):
                print("no hay alumnos cargados.")
            else:
                print("")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("nombre   /  genero  /   legajo | Matematica  /  Programacion  /  Arq. y Sistemas Op  /   Ingles   /  Met. de estudio")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                imprimir_datos(nombres, generos, legajos, notas, cant_alumnos)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    print("")
                    continue
        case 3:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("3. Buscar alumno")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            legajo = buscar("buscar legajo: ", legajos)
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("nombre   /  genero  /   legajo | Matematica  /  Programacion  /  Arq. y Sistemas Op  /   Ingles   /  Met. de estudio  /  Promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            imprimir_dato(nombres, generos, legajos, notas, legajo, promedios)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
        case 4:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("4. Mayores Promedios")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("nombre   /  genero  /   legajo | Matematica  /  Programacion  /  Arq. y Sistemas Op  /   Ingles   /  Met. de estudio  /  Promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            ordenar_descendente(nombres, generos, promedios, legajos)
            imprimir_datos(nombres, generos, legajos, notas, cant_alumnos, promedios)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    continue
        case 5:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("5. Materias con mayor promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            promedio_mayor(promedios_materias)
            ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
        case 6:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("6. Cantidad de notas por materia")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            repeticiones_notas(notas)
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
            break
        case 7:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("7. Salir")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            break

