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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from operator import itemgetter
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newdicc(tipo):
 
    diccio = {'videos': None,
               'categorias': None,
               }


    diccio['videos'] = lt.newList(tipo)

 
    diccio['categorias'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   )

    return diccio



# Funciones para agregar informacion al catalogo

def addVideo(diccio, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(diccio['videos'], video)


def addCategoria(diccio, videos):
    categorias = videos["category_id"]
    x = mp.contains(diccio["categorias"],categorias)
    if x:
        par = mp.get(diccio['categorias'], categorias)
        lis = me.getValue(par)
        
    else:
        lis = lt.newList()
        mp.put(diccio['categorias'], categorias,lis)

    lt.addLast(lis,videos)

def videosLikes(diccio, videos):
    categorias = videos["category_id"]
    x = mp.contains(diccio["categorias"],categorias)
    if x:
        par = mp.get(diccio['categorias'], categorias)
        lis = me.getValue(par)
        lis = me.getValue(cmpbylikes(videos["likes"],videos["likes"]))
           
    else:
        lis = lt.newList()
        mp.put(diccio['categorias'], categorias,lis)

    lt.addLast(lis,videos)




# Funciones para creacion de datos


# Funciones utilizadas para comparar elementos dentro de una lista
   

def cmpVideosByViews(video1, video2):

    return (float(video1['views']) > float(video2['views']))

def cmpPaisesbyviews(ll1,ll2):

    return(float(ll1["views"])>float(ll2["views"]))

def cmpCategoriesByTrending(cat1, cat2):

    return (float(cat1['title']) > float(cat2['title']))

def cmpbylikes(lili1,lili2):

    return(float(lili1["likes"])>float(lili2["likes"]))


# Funciones de ordenamiento


def Ordenamientos(tipo,dicci,size):

    start_time = time.process_time()
    sub_list= lt.subList(dicci["videos"],0,size)
    sub_list = sub_list.copy()

    if tipo == "shell":
        x = sa.sort(sub_list,cmpVideosByViews)
    elif tipo == "selection":
        x = sel.sort(sub_list,cmpVideosByViews)
    elif tipo == "insertion":
        x = ins.sort(sub_list,cmpVideosByViews)
    elif tipo == "quick":
        x = qk.sort(sub_list,cmpVideosByViews)
    elif tipo == "merge":
        x = mg.sort(sub_list,cmpVideosByViews)
    else:
        print("Este tipo de ordenamiento no existe")
    
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return x, elapsed_time_mseg


# Funciones de consulta
  
def paises(dicci):

    pass


def requerimiento1(dicci,ppais:str,categorias:str,cantidad:int):
    pass
    
def TrendingVideo(dicci,pais:str):

    pass  

def requerimiento3(dicci,categorii:str):

    pass
def organizartags(dicci):

    pass
def requerimiento4(dicci,tag:str,numero:int):
    pass