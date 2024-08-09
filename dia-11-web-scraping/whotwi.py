# modulos necesarios para web scraping
import bs4            # biblioteca que facilita extraer información de páginas web
import requests       # biblioteca HTTP simple pero elegante
import urllib.request # biblioteca extensible para abrir URLs
import urllib.error
import os
import webbrowser



# ingresar username
username = input("Ingresa username de Twitter: ")



# abrir whotwi, esto habilita la busqueda del username en la web whotwi por si fuera el caso que nadie la busco antes
webbrowser.open(f'https://es.whotwi.com/{username}/tweets/media')

# preguntar si continua el script o no
continuar = input("¿Desea continuar? Y/n: ")

if continuar.lower() == "y":
    print("Continuando con el script...")
else:
    print("Saliendo del script...")
    exit()



# crear url sin numero de pagina
url_base = 'https://es.whotwi.com/username/tweets/media?&page={}'

# reemplazar "username" en la url base con el valor de la variable "username"
url_base = url_base.replace("username", username)

# lista de fotos
list_fotos = []



# verificar carpetas
# ruta_fotos = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads\\fotos_twitter')
# ruta_username = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads\\fotos_twitter', username)
ruta_fotos = os.path.join('D:\\5 Escritorio\\KKK\\Twitter\\fotos_twitter')
ruta_username = os.path.join('D:\\5 Escritorio\\KKK\\Twitter\\fotos_twitter', username)

# recorrer lista de rutas
for ruta in [ruta_fotos, ruta_username]:
    # validar si la carpeta existe
    if not os.path.isdir(ruta):
        # si no existe, crear la carpeta
        os.makedirs(ruta)
        print("Carpeta creada exitosamente.", ruta)
    else:
        print("La carpeta ya existe.", ruta)



# iterar paginas
for pagina in range(1, 101): # range(1, 101)
    print("Pagina:", pagina)

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado  = requests.get(url_pagina)
    sopa       = bs4.BeautifulSoup(resultado.text, 'lxml')

    # verificar
    # print("URL Pagina:"    , url_pagina)
    # print("Resultado:"     , resultado)
    # print("Resultado text:", resultado.text)
    # print("Sopa:"          , sopa)

    # seleccionar datos de las fotos
    fotos = sopa.select('ul.media_list li')

    # verificar si no existen fotos en la pagina, termina la iteracion de paginas
    if len(fotos) == 0:
        break

    # iterar fotos
    for index, foto in enumerate(fotos):
        # print('index', index)
        # print('photo', foto)

        # seleccionar img
        img = foto.select_one('img') # select_one se puede utilizar para seleccionar un solo elemento en Beautiful Soup. Si la consulta devuelve varios elementos, se devuelve solo el primero. Si la consulta no devuelve ningún elemento, se devuelve None.

        # seleccionar post
        post = foto.select_one('a')

        # verificar que exista una etiqueta img
        if img:
            # guardar url en variable
            urlimg = img['src']
            urlpost = post['href']

            # obtener diccionario
            data = {'urlimg': urlimg, 'urlpost': urlpost}

            # agregar diccionario a la lista
            list_fotos.append(data)
        else:
            print('No se encontró la imagen en la foto', index)

# verificar
# print('list_fotos', list_fotos)

# iterar fotos
for index, foto in enumerate(list_fotos):
    print('index', index)
    print('photo', foto)

    # validar si la url tiene https
    if not foto['urlimg'].startswith('https://'):
        # agregar https a la url
        foto['urlimg'] = 'https:' + foto['urlimg']

    # validar si la url tiene https
    if not foto['urlpost'].startswith('https://'):
        # agregar https a la url
        foto['urlpost'] = 'https:' + foto['urlpost']

    # guardar imagen a partir de una url usando urllib
    urlimg = foto['urlimg']
    urlpost = foto['urlpost']
    # filename = f"C:\\Users\\Ernesto\\Downloads\\fotos_twitter\\{username}\\{username}_{index}.jpg"
    filename = f"D:\\5 Escritorio\\KKK\\Twitter\\fotos_twitter\\{username}\\{username}_{index}.jpg"

    try:
        urllib.request.urlretrieve(urlimg, filename)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"La imagen {urlimg} no se encontró en el servidor.")
        else:
            print(f"Error al descargar la imagen {urlimg}: {e}")
        continue  # saltar a la siguiente imagen en caso de error

    # si existe video crear acceso directo
    if 'video' in urlimg:
        # ruta del archivo de acceso directo
        # shortcut_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads\\fotos_twitter', username, f'{username}_{index}.url')
        shortcut_path = os.path.join('D:\\5 Escritorio\\KKK\\Twitter\\fotos_twitter', username, f'{username}_{index}.url')

        # verificar ruta
        # print('shortcut_path', shortcut_path)

        # crear el archivo de acceso directo
        with open(shortcut_path, 'w') as f:
            f.write("[InternetShortcut]\n")
            f.write("URL=" + urlpost + "\n")
