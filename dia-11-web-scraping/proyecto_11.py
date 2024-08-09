# modulos necesarios para web scraping
import bs4      # biblioteca que facilita extraer información de páginas web
import requests # biblioteca HTTP simple pero elegante



# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []



# iterar paginas
for pagina in range(1, 51): # range(1, 51)
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

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # agregamos lista dentro de la lista para guardar titulos por pagina
    titulos_rating_alto.append([])
    # titulos_rating_alto[pagina-1].append(f'Pagina {pagina}')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title'] # Obtiene la propiedad "title" del la etiqueta "a". Dentro de .product_pod, la web tiene dos etiquetas "a", por eso usamos [1], accedemos a la segunda etiqueta "a".
            # titulo_libro = libro.select('a')[1].text   # Obtiene el "text" de la etiqueta "a". La web "toscrape.com" en titulos grandes lo esta recortando con un "...".

            # agregar libro a la lista
            # titulos_rating_alto.append(titulo_libro)

            # agregar libro a la lista dentro de la lista, que representa la pagina actual
            titulos_rating_alto[pagina-1].append(titulo_libro)



# ver libros 4 u 5 estrellas en consola

# metodo "index" para obtener el indice numerico de la lista
# revisar "09-listas" de "1-aprendiendo-python"
'''
for pagina in titulos_rating_alto:
    print(f"\nPagina {titulos_rating_alto.index(pagina)+1}\n")
    for t in pagina:
        print(t)
'''

# metodo "enumerate" para obtener el indice numerico de la lista
# https://parzibyte.me/blog/2020/04/22/python-recorrer-lista-indice/
for indice, pagina in enumerate(titulos_rating_alto):
    print(f"\nPagina {indice+1}\n")
    for t in pagina:
        print(t)
