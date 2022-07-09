#EJERCICIO 1

from cgi import print_arguments
from posixpath import split
from warnings import filters


def articulosDeProvincia(nombreArchivo, provincia):
    listaPrecios=open(nombreArchivo)

    diccionarioArticulos = {}

    for linea in listaPrecios:
        lineaSplit = linea.split(",")
        if lineaSplit[1] == provincia:
            diccionarioArticulos[lineaSplit[0]] = float(lineaSplit[2])
    listaPrecios.close()
    return diccionarioArticulos




articulosMendoza = articulosDeProvincia("./lista_precios.csv", "Mendoza")
articulosCordoba = articulosDeProvincia("./lista_precios.csv", "Cordoba")




#EJERCICIO 2


conjuntoMendoza = set(articulosMendoza.keys())
conjuntoCordoba = set(articulosCordoba.keys())




def articulosCompartidos(dicProvincia1, dicProvincia2):
    conjprovincia1 = set(dicProvincia1.keys())
    conjprovincia2 = set(dicProvincia2.keys())
    compartidos = list(conjprovincia1 & conjprovincia2)
    return compartidos





MendozaYCordoba = articulosCompartidos(articulosMendoza,articulosCordoba)
print("Compartidos Mendoza y Cordoba : \n", MendozaYCordoba)
print("")


#EJERCICIO 3



def filtrarDiccionario (dicProvincia, listaArticulos):
    listaPrecios = []
    for articulo in listaArticulos:
        if articulo in dicProvincia:
            listaPrecios.append(dicProvincia[articulo])
    return listaPrecios        



listaDePrecios = filtrarDiccionario(articulosMendoza, MendozaYCordoba )

print("Lista de precios : \n", listaDePrecios)
print("")

#EJERCICIO 4
listaParaIterar = list(listaDePrecios)


def mayorMenor(elem): 
    return elem>100 and elem<200


def filtrarPrecios(lPrecios):
    preciosA = []
    for precio in lPrecios:
            if precio >100 and precio <200:
                preciosA.append(precio)
                
    return preciosA


def filtrarPreciosConFilter(lPrecios):
    
    preciosC = list(filter(mayorMenor, lPrecios))
    
    return preciosC







preciosFiltrados = filtrarPrecios(listaParaIterar)
preciosFiltradosB = filtrarPreciosConFilter(listaParaIterar)



print("Precios con FOR : \n"  , preciosFiltrados)
print("")
print("Precios con FILTER : \n", preciosFiltradosB)





