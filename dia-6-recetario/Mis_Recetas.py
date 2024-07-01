# MODULOS
import os                # Modulo para rutinas de sistemas operativos
from pathlib import Path # Modulo para acceder a rutas y ficheros
from os import system    # Modulo para rutinas de sistemas operativos


# METODO ORIGINAL
# mi_ruta = Path(Path.home(), "Recetas")

# METODO MODIFICADO
# https://www.delftstack.com/es/howto/python/python-get-path/
mi_ruta = Path(Path(__file__).parent.absolute(), "Recetas") # Ruta del archivo actual, obtenemos el archivo padre, y luego la ruta absoluta del archivo padre, luego completamos con lo que este dentro de las comillas ("")

# VERIFICAMOS RUTA
# print("Verificamos ruta", mi_ruta)
# exit()


# FUNCIONES
# Funcion para contar cantidad de archivos .txt recursivamente en una ruta
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Funcion para verificar cantidad de archivos .txt recursivamente en una ruta
def verificar_recetas(ruta):
    print("\nVerificar cantidad de archivos .txt recursivamente en una ruta")
    for txt in Path(ruta).glob("**/*.txt"):
        print(txt)
    print()

# Funcion que se ejecuta al iniciar el programa
def inicio():
    system('cls') # Limpia consola
    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en la ruta: {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")
    # verificar_recetas(mi_ruta)

    # Si "eleccion_menu" no es numerico, entrara en el bucle
    # Si "eleccion_menu" no esta en el rango de 1 a 7, entrara en el bucle
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear categoria nueva
        [3] - Eliminar categoria
        [4] - Crear receta nueva
        [5] - Eliminar receta
        [6] - Salir del programa''')
        print()
        eleccion_menu = input()

    return int(eleccion_menu)


# CATEGORIAS
# Funcion para mostrar categorias (Nombres de las carpetas dentro de la carpeta "Recetas")
def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir(): # Iterar los directorios de la ruta
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    # print("Verificamos categorias")
    # print(lista_categorias)
    return lista_categorias

# Funcion para preguntar que categoria eliges
def elegir_categoria(lista):
    # Si "eleccion_correcta" no es numerico, entrara en el bucle
    # Si "eleccion_correcta" no esta en el rango de 1 a x, entrara en el bucle
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")
    return lista[int(eleccion_correcta) - 1]


# RECETAS
# Funcion para mostrar recetas de las categorias
def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'): # Iterar los archivos .txt
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    # print("Verificamos recetas")
    # print(lista_recetas)
    return lista_recetas

# Funcion para preguntar que receta eliges
def elegir_recetas(lista):
    # Si "eleccion_receta" no es numerico, entrara en el bucle
    # Si "eleccion_receta" no esta en el rango de 1 a x, entrara en el bucle
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")
    return lista[int(eleccion_receta) - 1]

# Funcion para leer contenido de un archivo .txt
def leer_receta(receta):
    print(Path.read_text(receta))


# OPERACIONES CRUD
def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(F"La categoria {categoria.name} ha sido eliminada")

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

# OTRAS FUNCIONES
def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")


# INICIO DEL PROGRAMA
# Not es como el signo exclamación en PHP.
# https://es.stackoverflow.com/questions/281180/qu%C3%A9-funci%C3%B3n-hace-delante-de-una-condici%C3%B3n
finalizar_programa = False
while not finalizar_programa:
    menu = inicio()

    # Opciones
    if menu == 1: # Leer receta
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2: # Crear categoria nueva
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 3: # Eliminar categoria
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 4: # Crear receta nueva
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 5: # Eliminar receta
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 6: # Salir del programa
        finalizar_programa = True
