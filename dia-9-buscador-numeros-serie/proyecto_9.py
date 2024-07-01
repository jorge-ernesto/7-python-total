# MODULOS
import re                # Modulo que brinda soporte para expresiones regulares (RE).
import os                # Modulo para rutinas de sistemas operativos
import time              # Modulo de fecha
import datetime          # Modulo de feca
from pathlib import Path # Modulo para acceder a rutas y ficheros
import math              # Modulo que proporciona acceso a las funciones matemáticas



# OBTENEMOS FECHA EN FORMATO UNIX TIMESTAMP
inicio = time.time()
print()
print("Fecha UNIX timestamp:", inicio)
# exit()

# RUTA ORIGINAL
'''
Se puede usar '/' en lugar de '\\'
'''
# ruta = 'C:\\Users\\Usuario\\Desktop\\Mi_Gran_Directorio'

# RUTA MODIFICADA
'''
Se puede usar '/' en lugar de '\\'
'''
ruta = 'D:\\PORTABLES\\laragon\\www\\master-python\\2-python-total\\dia-9-buscador-de-numeros-de-serie\\Archivo ZIP\\Mi_Gran_Directorio'

# DETERMINAMOS PATTERN DE EXPRESION REGULAR
'''
A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
- [N] + [tres carateres de texto] + [-] + [5 números]

Sintaxis de las expresiones regulares
https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
Buscar \D
Buscar \d
Buscar {n}
'''
mi_patron = 'N\D{3}-\d{5}' # Originalmente tenia una r por delante, r'N\D{3}-\d{5}', esa r no tiene utilidad realmente

# OBTENEMOS FECHA ACTUAL
'''
Fechas con Python
https://codigofacilito.com/articulos/fechas-python
'''
hoy = datetime.date.today()
print("Fecha actual:", hoy)
print()
# exit()

# LISTA PARA ALMACENAR STRING QUE COINCIDA CON EL PATRON DE SERIE-NUMERO
nros_encontrados = []

# LISTA PARA ALMACENAR LOS ARCHIVOS DONDE SE ENCONTRARON LOS STRING DE SERIE-NUMERO
archivos_encontrados = []



# FUNCIONES
'''
Buscamos dentro de un archivo el patron SERIE-NUMERO
'''
def buscar_numero(archivo, patron):
    '''
    Metodo "open":
        Función abre un archivo y lo devuelve como un objeto de archivo.
        https://www.w3schools.com/python/ref_func_open.asp

    Metodo "re.search":
        Un RegEx, o expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda.
        RegEx se puede usar para verificar si una cadena contiene el patrón de búsqueda especificado.
        https://www.w3schools.com/python/python_regex.asp
    '''
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

'''
Buscamos recursivamente en la carpeta "Mi_Gran_Directorio" todos los archivos
y luego buscamos dentro de cada archivo si el contenido coincide con el patron SERIE-NUMERO
'''
def crear_listas():
    # print("Metodo walk", os.walk(ruta))
    # for x in os.walk(ruta):
    #     print("\n", x)

    '''
    Metodo "os.walk":
        Usamos el metodo para obtener recursivamente todos los archivos dentro de "Mi_Gran_directorio",
        armamos la ruta de los archivos mencionados y buscamos en el archivo si existe el patron SERIE-NUMERO
        http://www.tugurium.com/python/index.php?C=PYTHON.12_1_1#:~:text=El%20m%C3%A9todo%20walk()%20nos,Nombre%20de%20la%20carpeta%20actual.
    El metodo retorna:
        1. Ruta de la carpeta actual
        2. Lista de carpetas dentro de la carpeta actual
        3. Ficheros de la carpeta actual
    '''
    for carpeta, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group()) # .group() devuelve la parte de la cadena donde hubo una coincidencia
                archivos_encontrados.append(a.title()) # Bien podria usarse solo a

'''
Mostramos información
'''
def mostrar_todo():
    '''
    Fechas con Python
    https://codigofacilito.com/articulos/fechas-python
    '''
    fecha_formateada = hoy.strftime('%d/%m/%Y')
    # print(fecha_formateada)

    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {fecha_formateada}') # Antes estaba asi ----> print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')                # \t es una tabulación
    print('-------\t\t\t----------')                # \t es una tabulación
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encontrados: {len(nros_encontrados)}')
    fin = time.time()                              # Obtenemos nuevamente la fecha en formato UNIX timestamp
    duracion = fin - inicio                        # Obtenemos el tiempo de ejecución del script
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)



# INICIO DEL PROGRAMA
crear_listas()
mostrar_todo()
