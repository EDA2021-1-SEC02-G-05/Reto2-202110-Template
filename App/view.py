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
    print("2-  Organizar los videos por categorias")
    print("3- videos con mas likes ")
    print("4- Consultar los videos con mas tendencia por catehoria de un pais ")
    print("5- Consultar el video mas trending por pais ")
    print("6- Consultar el video mas trending por categoria")
    print("7- los video con mas likes en un pais con un cierto tag")
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

def loaddpaises(diccio,pais,categoriaa,numero):

    return controller.loadpaises(diccio,pais,categoriaa,numero)

def loadPaises(diccio):

    return controller.loadPais(diccio)

def loaddorganizartags(diccio):

    return controller.loadorganizartags(diccio)


def loaddrequerimiento2(diccio,pais):

    return controller.loadrequerimiento2(diccio,pais)


def loaddrequerimiento3(diccio,categoria):

    return controller.loadrequerimiento3(diccio,categoria)

def loaddrequerimiento4(diccio,country,numero,tag):
    return controller.loadrequerimiento4(diccio,country,numero,tag)

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
        tutu=loaddorganizartags(diccio)
        so=controller.loadPais(diccio)

        primer= lt.firstElement(diccio["videos"])
        lista=[]
        
        print('Videos cargados: ' + str(lt.size(diccio['videos'])))
        print("el primer video: "+" Titulo : "+str(primer["title"])+" , "+" Nombre del canal:  "+str(primer["channel_title"])+" , "+" Fecha de tendencia: "+str(primer["trending_date"])+" , " +" Pais: "+str(primer["country"])+" , "  + " Vistas: "+str(primer["category_id"])+" , "+"  Me gustas: "+str(primer["likes"])+", "+ "Nomegustas :"+str(primer["category_id"]))

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

    elif  int(inputs[0]) == 4:  
        pais=str(input(" Ingrese el nombre del pais de su interes: "))
        categoriaa=str(input(" Ingrese el nombre de la categoria de su interes: "))
        numero=int(input( " Ingrese el numero de videos el cual esta interesado: "))


        badbunny=loaddpaises(diccio,pais,categoriaa,numero)
        print("Tiempo [ms]: ", f"{badbunny[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{badbunny[2]:.3f}")

        print(badbunny)

    elif int(inputs[0]) == 5:

        pais=str(input(" Ingrese el nombre del pais que esta interesado:  "))


        benzema =loaddrequerimiento2(diccio,pais)
        

        print(benzema)
        print("Tiempo [ms]: ", f"{benzema[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{benzema[2]:.3f}")

    elif int(inputs[0]) == 6:

        categoria=str(input(" Ingrese el nombre de la categoria de su interes: "))

        celjas=loaddrequerimiento3(diccio,categoria)
        print("Tiempo [ms]: ", f"{celjas[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{celjas[2]:.3f}")


        print(celjas)


    elif int(inputs[0]) == 7:



        country=str(input(" Ingrese el nombre de la pais de su interes: "))
        tag=str(input( " Ingrese  el tag que esta interesado en buscar:  "))
        numero=int(input(" Ingrese el numero de videos que quiere ver : "))




        ramiro=loaddrequerimiento4(diccio,country,numero,tag)
        print("Tiempo [ms]: ", f"{ramiro[1]:.3f}", " || ",
        "Memoria [kB]: ", f"{ramiro[2]:.3f}")

        print(ramiro)





    



       
  

    else:
        sys.exit(0)

sys.exit(0)