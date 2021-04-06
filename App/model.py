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
from DISClib.DataStructures import listiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newdicc(tipo,tipo2,num):
 
    diccio = {'videos': None,
               'categorias': None,
               }


    diccio['videos'] = lt.newList(tipo)
 
    diccio['categorias'] = mp.newMap(10000,
                                   maptype=tipo2,
                                   loadfactor=num,
                                   )

    return diccio



# Funciones para agregar informacion al catalogo

def addVideo(diccio, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(diccio['videos'], video)




def addCategoria(diccio):


    for m in range(0,lt.size(diccio["videos"])):
        rta=lt.getElement(diccio["videos"],m)

        rta["category_id"]


        if mp.contains(diccio["categorias"],rta["category_id"])== True:
         
            par = mp.get(diccio['categorias'], rta["category_id"])
            lis = me.getValue(par)

            lt.addLast(lis,rta)
            mg.sort(lis,cmpbylikes)
        
        else:
            lis = lt.newList()
            mp.put(diccio['categorias'],rta["category_id"],lis)
            lt.addLast(lis,rta)

    return diccio        

def videosLikes(diccio,numero,categor):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    lol=categori[categor]

    lola=[] 

    
    par = mp.get(diccio['categorias'],str(lol))
    lis = me.getValue(par)

    for i in range(numero):


        tt=lt.getElement(lis,i)

        lola.append(tt)

    return lola
        

    

    

    












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