# MODULOS
import numeros


# FUNCIONES
def preguntar():
    print("Bienvenido a Farmacia Python")

    # Revisar "15-manejo-errores" de "1-aprendiendo-python"
    # try   : Ejecutamos esta porcion de codigo
    # except: Ha ocurrido un error
    # else  : Todo ha funcionado correctamente
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break # Esto libera el bucle while

    # Ejecutamos generadores segun rubro elegido
    numeros.decorador(mi_rubro)

def inicio():
    # Preguntamos el rubro para generar los turnos
    preguntar()

    # Revisar "15-manejo-errores" de "1-aprendiendo-python"
    # try   : Ejecutamos esta porcion de codigo
    # except: Ha ocurrido un error
    # else  : Todo ha funcionado correctamente
    while True:
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "S":
                preguntar() # Volvemos a preguntar
            elif otro_turno == "N":
                print("Gracias por su visita")
                break # Esto libera el bucle while


# INICIO DEL PROGRAMA
inicio()
