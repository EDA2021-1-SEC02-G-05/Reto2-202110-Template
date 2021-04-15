"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import tracemalloc
import config as cf
import model
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initdicci(tipo,tipo2,num):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    diccio = model.newdicc(tipo,tipo2,num)
    return diccio

# Funciones para la carga de datos

def loadData(diccio):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(diccio)
    loadCategorias(diccio)
    
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def loadVideos(diccio):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videofile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(diccio, video)
    
def loadorganizartags(diccio):

    james=model.organizartags(diccio)

    return james

   

# Funciones de consulta sobre el catálogo

def loadaddcategoria(diccio):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()


    agustinjulio=model.addCategoriaa(diccio)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory , agustinjulio


def loadCategorias(diccio):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    dialect = csv.excel()
    dialect.delimiter = "\t"
    catfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(catfile,encoding='utf-8'),dialect=dialect)
    for cat in input_file:
        model.addCategoria(diccio, cat)
        print(cat)

def loadvideosLikes(diccio,numero,categor):

    omarperez=model.videosLikes(diccio,numero,categor)

    return omarperez


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

def loadpaises(diccio,pais,categoriaa,numero):

    gerardopeluso=model.paises(diccio,pais,categoriaa,numero)

    return gerardopeluso


def loadPais(diccio):

    vela=model.addPais(diccio)

    return vela


def loadrequerimiento2(diccio,pais):

    trenvalencia=model.requerimiento2(diccio,pais)

    return trenvalencia


def loadrequerimiento3(diccio,categoria):

    nani=model.requerimiento3(diccio,categoria)

    return nani


def loadrequerimiento4(diccio,country,numero,tag):
    paul=model.requerimiento4(diccio,country,numero,tag)

    return paul


    