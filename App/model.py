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
 
    diccio['categorias'] = mp.newMap(100,
                                   maptype=tipo2,
                                   loadfactor=num,
                                    )

    diccio["paises"]= mp.newMap(100,
                                   maptype=tipo2,
                                   loadfactor=num
                                   )
    diccio['category']= mp.newMap(100,
                                   maptype=tipo2,
                                   loadfactor=num,
                                   comparefunction=cmpbyId)
    diccio['trending']= mp.newMap(100,
                                   maptype=tipo2,
                                   loadfactor=num,
                                   comparefunction=cmpbyId)


 

    return diccio



# Funciones para agregar informacion al catalogo

def addVideo(diccio, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(diccio['videos'], video)

def addCategoria(diccio, cat):
    # Se adiciona la categoria a la lista de categorias

    mp.put(diccio["category"],cat["name"],cat["id"])


def organizartags(diccio):
    pala=""
    lista=[]
    ll=[]
    
    for i in range(0,lt.size(diccio["videos"])):

        rta=lt.getElement(diccio["videos"],i) 

        for mm in rta["tags"]:

            if mm != "|"and  mm!='"':

                pala+=mm
            else:
                lista.append(pala)
                pala=""

        for pp in lista:

             if pp !='':

        
                 ll.append(pp)


        
        rta["tags"]=ll
        ll=[]

      
    return diccio






def addCategoriaa(diccio):

    iterador = it.newIterator(diccio["videos"])

    while it.hasNext(iterador):
        actual = it.next(iterador)
        
        actual["category_id"]


        if mp.contains(diccio["categorias"],actual["category_id"])== True:
         
            par = mp.get(diccio['categorias'], actual["category_id"])
            lis = me.getValue(par)

            lt.addLast(lis,actual)
        
        else:
            lis = lt.newList()
            mp.put(diccio['categorias'],actual["category_id"],lis)
            lt.addLast(lis,actual)

    return diccio        



#arreglar
def videosLikes(diccio,numero,categor):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    lol=categori[categor]

    lola=[] 

    
    par = mp.get(diccio['categorias'],str(lol))
    lis = me.getValue(par)
    lis=mg.sort(lis,cmpbylikes)


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

def cmpbyId(id1,id2):

    ID2 = me.getKey(id2)

    if id1 == ID2:
        return 0
    elif id1 > ID2:
        return 1
    else:
        return -1

def cmpbyId2(id1,id2):

    ID2 = me.getKey(id2)

    if int(id1) == int(ID2):
        return 0
    elif int(id1) > int(ID2):
        return 1
    else:
        return -1



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




 
  
def paises(diccio,pais,categoriaa,numero):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    categoriaa=str(categori[categoriaa])


    par = mp.get(diccio['categorias'],str(categoriaa))
    lis = me.getValue(par)
    lis=mg.sort(lis,cmpPaisesbyviews)

    iterador = it.newIterator(lis)

    while it.hasNext(iterador):

        actual = it.next(iterador)
        
        if actual["country"]== pais:
            listt = lt.newList()
            mp.put(diccio['paises'],actual["country"],listt)
            lt.addLast(listt,actual)

    parra = mp.get(diccio['paises'],pais)
    toloza = me.getValue(parra)

    chicharo=[]


    iteradorr = it.newIterator(toloza)


    while it.hasNext(iteradorr):
        acto = it.next(iteradorr)

        chicharo.append(acto)

    chicharo=chicharo[:numero]

    return chicharo


def addPais(diccio):

    iterador = it.newIterator(diccio["videos"])

    while it.hasNext(iterador):

        actual = it.next(iterador)
        if mp.contains(diccio["trending"],actual["country"])==True:

            par = mp.get(diccio['trending'], actual["country"])
            lis = me.getValue(par)

            lt.addLast(lis,actual)

        else:
            lis = lt.newList()
            mp.put(diccio['trending'],actual["country"],lis)
            lt.addLast(lis,actual)

    return diccio 


def requerimiento2(diccio,pais:str):

    diccionario = {}

    par = mp.get(diccio['trending'], pais)
    lis = me.getValue(par)

    iterador = it.newIterator(lis)

    while it.hasNext(iterador):

        actual = it.next(iterador)

        if actual["title"] in diccionario:
            diccionario[actual["title"]][0]+=1

        else:
            diccionario[actual["title"]]=[1,(actual)]

    numero = 0

    for i in diccionario:
        if diccionario[i][0] > numero:
            numero= diccionario[i][0]
            tt=(("El titulo del video : "+str(diccionario[i][1]["title"])," El nombre del canal: "+str(diccionario[i][1]["channel_title"]),"el category id: "+str(diccionario[i][1]["category_id"]),"los dias que ha sido trending: "+str(diccionario[i][0])))



    return tt






def  requerimiento3(diccio,categoria):
    categori={"Film & Animation":1,"Autos & Vehicles":2,"Music":10,"Pets & Animals":15,"Sports":17,"Short Movies":18,"Travel & Events":19,"Gaming":20,"Videoblogging":21,"People & Blogs":22,"Comedyy":23,"Entertainment":24,"News & Politics":25,"Howto & Style":26,"Education":27,"Science & Technology":28,"Non-profits & Activism":29,"Movies":30,"Anime/Animation":31,"Classics":33,"Comedy":34,"Documentary":35,"Drama":36,"Family":37,"Foreign":38,"Horror":39,"Sci-Fi/Fantasy":40,"Thriller":41,"Shorts":42,"Shows":43,"Trailers":44}
    categoria=str(categori[categoria])

    diccionario={}


    par = mp.get(diccio['categorias'], categoria)
    lis = me.getValue(par)

    iterador = it.newIterator(lis)

    while it.hasNext(iterador):

        actual = it.next(iterador)

        if actual["title"] in diccionario:
            diccionario[actual["title"]][0]+=1

        else:
            diccionario[actual["title"]]=[1,(actual)]

    numero = 0

    for i in diccionario:
        if diccionario[i][0] > numero:
            numero= diccionario[i][0]
            tto=(("El titulo del video : "+str(diccionario[i][1]["title"])," El nombre del canal: "+str(diccionario[i][1]["channel_title"]),"el category id: "+str(diccionario[i][1]["category_id"]),"los dias que ha sido trending: "+str(diccionario[i][0])))

    return tto


def requerimiento4(diccio,country,numero,tag ):
    lastima=[]


    par = mp.get(diccio['trending'], str(country))
    lis = me.getValue(par)
    lis=mg.sort(lis,cmpbylikes)



    iterador = it.newIterator(lis)

    while it.hasNext(iterador):

        tt = it.next(iterador)


        if tag in tt["tags"]:


            lastima.append(("titulo: "+str(tt["title"])," Nombre del canal: "+str(tt["channel_title"])," Fecha de publicacion: "+str(tt["publish_time"])," Visitas: "+str(tt["views"])," Me gustas"+str(tt["likes"]),"No me gustas: "+str(tt["dislikes"])))



    lastima=lastima[:numero]
            
    return lastima










    












    














   












    pass


















