from Create_Graph import G
from Connections import Conexiones
from Recursive_Search import Recursive_Search as RS

import threading

def Enrutamiento(lista, Nodo):
    """Genera las rutas más cortas en lista saliendo desde Nodo
    >>> Enrutamiento(Conexiones, "241.12.31.14")
    ("241.12.31.14","241.12.31.15")
    ("241.12.31.14","241.12.31.15","241.12.31.16")
    ("241.12.31.14",241.12.31.18","241.12.31.17")
    ("241.12.31.14","241.12.31.18")
    ("241.12.31.14","241.12.31.19")
    """

    for node in G.nodes():

        if (node == Nodo): pass
        else:
            #thread = threading.Thread(name = node, target = RS, args = (Nodo, node))
            #thread.run()
            #thread.join()
            print(RS(Nodo, node, set()))
        

Enrutamiento(Conexiones, "241.12.31.14")



# import doctest
# doctest.testmod()
