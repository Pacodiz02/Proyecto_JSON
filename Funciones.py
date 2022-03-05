# Funciones JSON

import json

# Función leer JSON

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
        return datos
    except:
        print("Error al leer el fichero")


# 1. Función para listar el nombre de las peliculas.

def nombre_pelis(datos):
    lista=[]
    for a in datos:
        lista.append(a.get("name"))
    return lista


# 2. Función para contar peliculas de un guionista.

def contar_pelis(datos,nombreguio):
    cont = 0
    for a in datos:
        for guio in a.get("writer"):
            if guio == nombreguio:
                cont=cont+1
    return cont


# 3. Función para filtrar peliculas por un año.

def pelis_anio(datos,anio_introducido):
    listapelis=[]
    for a in datos:
        anios=a.get ("year")
        if anios == anio_introducido:
            listapelis.append(a.get("name"))
    return listapelis


# 4. Función para ver las pelis de un director.

def pelis_director(datos,director):
    lista_director=[]
    for a in datos:
        nombredirector=a.get("director").get("name")
        if nombredirector == director:
            lista_director.append(a.get("name"))
    return lista_director
    
# 5. Función antiguedad.

def antiguedad(datos,anioactual,antiguedadanio):
    listaantig=[]
    for a in datos:
        anios=a.get("year")
        antig=anioactual-anios
        if antig == antiguedadanio:
            for e in a.get("actors"):
                listaantig.append([a.get("name"),e])
    return listaantig  



