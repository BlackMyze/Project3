from Create_Graph import G

def Recursive_Search(from_Node = None, to_Node = None, exceptions = set()):
    
    neighbors = [*G.neighbors(from_Node)]
    if (to_Node in neighbors): print(f'("{from_Node}","{to_Node}")'); return
    else:
        
        if (from_Node in exceptions): print(exceptions, 'esto es una excepcion'); return
        else:
            print(f'{from_Node} --> {to_Node}')
            exceptions.add(from_Node)

            for neighbor in neighbors:
                Recursive_Search(neighbor, to_Node, exceptions)
 

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
    

    
