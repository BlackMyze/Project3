from Create_Graph import G

def Recursive_Search(from_Node = None, to_Node = None, exceptions = set()):
    
    neighbors = [*G.neighbors(from_Node)]
    
    if (to_Node in neighbors): 
        #print(f'("{from_Node}","{to_Node}")')
        return f'{from_Node},{to_Node}'
    elif (from_Node in exceptions):  
        print(f'\n[ERROR]: {from_Node} --> {to_Node}')
        #return f'\tCamino no encontrado para el nodo {to_Node}\n' # Esto es lo que genera problema (arreglar pues)
    else:

        print('Esto es una recursión nueva', exceptions)
        exceptions.add(from_Node)
#        exceptions.update(neighbors)
        
        for neighbor in neighbors:
            print('entrando al for')
            return f'{from_Node}, {Recursive_Search(neighbor, to_Node, exceptions)}'
 

        # Creating the intersection between from_Node and to_Node
#        intersection = set(neighbors).intersection(set([*G.neighbors(to_Node)]))

        # Verify if there are in common between from_Node and to_Node
#        if (intersection): print(f'("{from_Node}","{intersection.pop()}","{to_Node}")');
#        else:
            
#            for neighbor in neighbors:
#                Recursive_Search(neighbor, to_Node, )

    #print(old_neighbors)
    #print(*G.neighbors(path[-1]))
    #print(*G.neighbors(to_Node))
    #    for old in old_neighbors:
    #    print(*G.neighbors(old))
    

    
