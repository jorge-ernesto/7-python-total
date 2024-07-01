# FUNCIONES


# Video 116. Generadores
# Los generadores son un tipo especial de funcion, que en vez de devolvernos un valor terminado, va produciendo ese valor poco a poco, a medida que lo vamos necesitando
# Palabra clave "yield", que quiere decir "producir", es necesario en las Funciones Generadores para entregar y recordar los valores uno a uno
def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


# Para producir los generadores los guardamos en variables
# Palabra clave "next", que quiere decir "siguiente", con next podemos acceder a nuestros generadores
p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


# Video 115. Decoradores
# Los decoradores son funciones que modifican el comportamiento de otras funciones y ayudan a acortar nuestro código
# La siguiente funcion no utiliza decoradores, al menos no del modo como se explico en el video
def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su número es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")
