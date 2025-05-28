def validar_nombre(nombre:str) -> bool:
    hay_error = False
    for i in nombre:
        if ord(i) >= 48 and ord(i) <= 57 or i == " ":
            hay_error = True

    return hay_error

def validar_genero(genero:str) -> bool:
    hay_error = False
    if genero != "M" and genero != "F" and genero != "X" and genero != "m" and genero != "f" and genero != "x":
        hay_error = True
    return hay_error

def validar_legajo(legajo:str, legajos_existentes:list) -> bool:
    hay_error = False
    for i in legajo:
        if ord(i) >= 48 and ord(i) <= 57:
            if int(legajo) < 10000 or int(legajo) > 99999:
                hay_error = True
        else:
            hay_error = True
    for existente in legajos_existentes:
        if existente == legajo:
            hay_error = True
    return hay_error

def validar_opcion(opcion:str) -> bool:
    hay_error = False
    for i in opcion:
        if ord(i) < 48 and ord(i) > 57:
            hay_error = True
    return hay_error

def validar_numero(numero:str) -> bool:
    hay_error = False
    for i in numero:
        if ord(i) >= 48 and ord(i) <= 57:
            if int(numero) < 1:
                hay_error = True
        else:
            hay_error = True
    return hay_error

def validar_nota(nota:str) -> bool:
    hay_error = False
    for i in nota:
        if ord(i) >= 48 and ord(i) <= 57:
            if int(nota) < 0 or int(nota) > 10:
                hay_error = True
    return hay_error