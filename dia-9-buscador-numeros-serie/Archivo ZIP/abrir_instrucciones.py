"""
Importamos modulo que nos sirva para poder descomprimir el archivo Proyecto+Dia+9.zip
"""
import shutil


"""
Usamos metodo shutil.unpack_archivo
Parametro 1: Nombre del archivo
Parametro 2: Ruta donde queremos descargar el archivo
Parametro 3: Tipo de archivo a descomprimir
"""
shutil.unpack_archive('Proyecto+Dia+9.zip', 'D:\\PORTABLES\\laragon\\www\\master-python\\2-python-total\\dia-9-buscador-de-numeros-de-serie\\Archivo ZIP', 'zip')
