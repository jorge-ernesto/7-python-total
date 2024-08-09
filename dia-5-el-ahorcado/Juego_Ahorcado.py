'''
Metodo "choise":
    Devuelve un elemento aleatorio de una lista.
    https://www.w3schools.com/python/ref_random_choice.asp

Metodo "set":
    Convierte un string en una colección de datos tipo 'set', se eliminan los caracteres que se repiten. También existen otros metodos como el metodo 'list'.
    https://www.w3schools.com/python/python_datatypes.asp

        SET en un tipo de dato, para tener una coleccion de valores,
        pero no tiene ni indice ni orden

        Diccionario:
        Un tipo de dato que almacena un conjunto de datos.
        En forma clave > valor.
        Es parecido a un array asociativo o un objeto json.

Metodo "len":
    Devuelve el número de elementos en un objeto.
    https://www.w3schools.com/python/ref_func_len.asp
'''


# MODULOS
from random import choice


# VARIABLES
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_incorrectas = []
letras_correctas = []
intentos = 6
aciertos = 0
juego_terminado = False


# FUNCIONES
# Escogemos una palabra al asar y obtenemos la cantidad de caracteres unicos
def elegir_palbra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

# Recorremos palabra elegida y mostramos con guiones cada caracter
# Si hemos ingresado una letra correcta, mostramos letra ingresada en lugar de guiones
# La primera vez que se ejecuta la funcion, muestra todo en guiones
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

# Obtenemos letra ingresada
# Debe tener un solo caracter y debe ser una letra del alfabeto
# Si no se cumple, te pedira la letra hasta que se cumpla la condicion
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

# Verificamos si letra elegida esta dentro de la palabra oculta o no, para aumentar la cantidad de coincidencias o reducir una vida
# Determinamos si ganas o pierdes
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta: # VERIFICAMOS QUE LA LETRA ELEGIDA ESTE DENTRO DE LA PALABRA OCULTA
        if letra_elegida not in letras_correctas: # PARA AGREGARLA AL ARRAY DE LETRAS CORRECTAS, NO DEBE ESTAR DENTRO
            letras_correctas.append(letra_elegida)
            coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0: # SI YA NO HAY VIDAS, GANAS
        fin = perder()
    elif coincidencias == letras_unicas: # SI COINCIDENCIAS ES IGUAL A CANTIDAD DE CARACTERES UNICOS DE LA PALABRA OCULTA, PIERDES
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")
    return True


# INICIO DEL PROGRAMA
palabra, letras_unicas = elegir_palbra(palabras)

# print(f"""
# Verificamos palabra y cantidad de caracteres unicos
#     - Palabra: {palabra}
#     - letras_unicas: {letras_unicas}
# """)

# Not es como el signo exclamación en PHP.
# https://es.stackoverflow.com/questions/281180/qu%C3%A9-funci%C3%B3n-hace-delante-de-una-condici%C3%B3n
while not juego_terminado:
    print("\n---- TABLERO AHORCADO ----")
    print("\n" + "*" * 60)
    mostrar_nuevo_tablero(palabra)
    print(f"Letras incorrectas: {' '.join(letras_incorrectas)}") # La primera vez que se ejecuta el programa, muestra vacio
    print(f"Vidas: {intentos}")                                  # La primera vez que se ejecuta el programa, muestra 6 vidas
    print("*" * 60 + "\n")

    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado
