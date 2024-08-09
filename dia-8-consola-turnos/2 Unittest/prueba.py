"""
Para usar Unittest, no debemos instalar nada, viene incorporada con Python
Asi que solamente hay que importar el módulo "unittest"
También importamos el módulo "cambia_texto"
"""
import unittest
import cambia_texto


"""
Esta clase heredara de unittest.TestCase
Estamos heredando todos los metodos que tiene TestCase para poder usarlos en esta clase
"""
class ProbarCambiaTexto(unittest.TestCase):

    """
    Funcion que se encarga de hacer la verificación
    Importante que las funciones que haran las evaluaciones, es que deben comenzar con la palabra "test_", luego puedes poner el nombre que quieras
    """
    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        """
        assertEqual verificara si resultado es igual a 'BUEN DIA' escrito manualmente
        """
        self.assertEqual(resultado, 'BUEN DIA')


"""
Esto es una manera de que Python sepa que funcion debe ejecutar y cual no
Esta sección de código es necesaria para usar Unittest
"""
if __name__ == '__main__':
    unittest.main()
