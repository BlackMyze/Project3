from Create_Graph import G

def Recursive_Search(from_Node = None, to_Node = None, exceptions = set()):
    
    neighbors = [*G.neighbors(from_Node)]
    if (to_Node in neighbors): 
        #print(f'("{from_Node}","{to_Node}")')
				#return f'Path find from {from_Node} to {to_Node}')
        return f'{from_Node} --> {to_Node}'
    
    elif(from_Node in exceptions): pass
				#print(f'[ERROR]: {from_Node} --> {to_Node}')
        #return f'\tCamino no encontrado para el nodo {to_Node}\n' # Esto es lo que genera problema (arreglar pues)

    else:

        #print('Esto es una recursión nueva', exceptions, to_Node)
        exceptions.add(from_Node)
#        exceptions.update(neighbors)
        
        for neighbor in neighbors:
            #print('entrando al for')
            recursion = Recursive_Search(neighbor, to_Node, exceptions)
            
            if (recursion != None): return f'{from_Node} --> {recursion}'
 

