# Programa Principal JSON

from Funciones import *

peliculas=leer_json("FicheroJSON.json")


print('''
1. Lista el nombre de todas las películas.
2. Contar las peliculas en las que un guionista(writer) participó.
3. Filtrar peliculas por año.
4. Metemos un director y nos dice el nombre de las películas que ha dirigido.
5. Escribe una antiguedad(50,40,25 años) y mostrar las películas que tienen esa antiguedad con los actores que participan en ellas.
6. Salir''')

print("\n")

opcion=int(input("Introduce una opción: "))

print("\n")

while opcion !=6:

    if opcion == 1:
        for a in nombre_pelis(peliculas):
            print(a)


    elif opcion == 2:
        nombreguio=input("Introduce el nombre del guionista: ")
        print("\n")
        contar=contar_pelis(peliculas,nombreguio)
        print("El guionista %s apareció en %i películas." %(nombreguio,contar))


    elif opcion == 3:
        anio_introducido=int(input("Introduce un año: "))
        print("\n")
        filtrar_pelis_anio=pelis_anio(peliculas,anio_introducido)
        for a in filtrar_pelis_anio:
            print(a)
    
    elif opcion == 4:
        director=input("Introduce el nombre del director: ")
        print("\n")
        pelisdirector=pelis_director(peliculas,director)
        print("El director %s ha dirigido: %s" %(director,pelisdirector))

    elif opcion == 5:
        anioactual=int(input("Introduce el año actual: "))   
        antiguedadanio=int(input("Introduce una antiguedad(Ej. 50,60,70 años): "))
        anio_antiguedad= antiguedad(peliculas,anioactual,antiguedadanio)
        for a in anio_antiguedad:
            print(a)

    print("\n")
    print('''
    1. Lista el nombre de todas las películas.
    2. Contar las peliculas en las que un guionista(writer) participó.
    3. Filtrar peliculas por año.
    4. Metemos un director y nos dice el nombre de las películas que ha dirigido.
    5. Escribe una antiguedad(50,40,25 años) y mostrar las películas que tienen esa antiguedad con los actores que participan en ellas.
    6. Salir''')

    print("\n")
    
    opcion=int(input("Introduce una opción: "))
    
    print("\n")