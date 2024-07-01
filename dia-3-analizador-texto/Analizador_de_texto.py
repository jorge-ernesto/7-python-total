texto = input("Ingresa un texto a elección: ")
letras = []

'''
Metodo 'lower':
    Devuelve una cadena donde todos los caracteres están en minúsculas. Se ignoran los símbolos y los números.
    https://www.w3schools.com/python/ref_string_lower.asp
'''

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

# print(texto)
# print(letras)
# exit()

'''
Metodo 'count':
    Devuelve el número de veces que aparece el valor pasado como parametro en la cadena.
    https://www.w3schools.com/python/ref_string_count.asp
'''

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

# exit()

'''
Metodo 'split':
    Divide una cadena en una lista donde cada palabra es un elemento de la lista.
    https://www.w3schools.com/python/ref_string_split.asp
'''

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

# exit()

'''
Accedemos a la primera letra
Accedemos a la ultima letra
'''

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

# exit()

'''
Metodo 'reverse':
    Invierta el orden de los elementos de la lista.
    https://www.w3schools.com/python/ref_list_reverse.asp

Metodo 'join':
    Toma todos los elementos en un iterable y los une en una sola cadena.
    https://www.w3schools.com/python/ref_string_join.asp
'''

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

# exit()

print("\n")
print("VERIFICAMOS INFORMACION ACTUAL")
print('Texto ingresado:', texto)

# exit()

'''
Metodo 'in':
    Palabra clave se utiliza para verificar si un valor está presente en una secuencia (lista, rango, cadena, etc.). Devuelve True o False.
    https://www.w3schools.com/python/ref_keyword_in.asp
'''

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
