"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

assert cf
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*100) 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Indicar el tipo de ordenamiento")
    print("3- Organice los videos por paises")
    print("4- Consultar los videos mas vistas  por pais")
    print("5- Consultar los videos con mas trending")
    print("6- Consultar el video mas trending por categoria")
    print("7- Organizar los videos con sus tags")
    print("8- Consultar los videos por un tag")
    print("0- Salir")

def initdicci(tipo,tipo2,num):
    """
    Inicializa el catalogo de libros
    """
    return controller.initdicci(tipo,tipo2,num)

def loadData(diccio):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(diccio)

def loadaddcategoria(diccio):

    return controller.loadaddcategoria(diccio)

def loaddloadvideosLikes(diccio,numero,categor):

    return controller.loadvideosLikes(diccio,numero,categor)

diccio = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        x = str(input("Indique el tipo de lista que quiere entre ARRAY_LIST o SINGLE_LINKED: "))
        x2 = str(input("Indique el tipo de map que quiere entre CHAINING y PROBING: "))
        x3 = float(input("Indique el factor de carga deseado : "))
        diccio = initdicci(x,x2,x3)
        answer = controller.loadData(diccio)
        primer= lt.firstElement(diccio["videos"])
        lista=[]
        
        print('Videos cargados: ' + str(lt.size(diccio['videos'])))
        print("el primer video: "+" Titulo : "+str(primer["title"])+" , "+" Nombre del canal:  "+str(primer["channel_title"])+" , "+" Fecha de tendencia: "+str(primer["trending_date"])+" , " +" Pais: "+str(primer["country"])+" , "  + " Vistas: "+str(primer["category_id"])+" , "+"  Me gustas: "+str(primer["likes"])+", "+ "Nomegustas :"+str(primer["dislikes"]))

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", " || ",
        "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 2:   
        
        answer = controller.loadaddcategoria(diccio)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", " || ",
        "Memoria [kB]: ", f"{answer[1]:.3f}")

        print(" Se han organizado los videos por categorias ")

    elif int(inputs[0]) == 3:  

        nn=int(input(" Ingrese la cantidad de videos para ver: "))
        categor=str(input(" Ingrese el nombre de la categoria: "))
        jes=loaddloadvideosLikes(diccio,nn,categor)

        print(jes)


    


        

    else:
        sys.exit(0)

sys.exit(0)