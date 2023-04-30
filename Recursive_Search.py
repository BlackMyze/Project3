from Create_Graph import G

def Recursive_Search(exception_list=[], old_neighbors = [], to_Node = None):
    
    for old in old_neighbors:
        new_neighbord = set([*G.neighbors(old), old])
        new_neighbord = set(exception_list).symmetric_difference(new_neighbord)
        new_neighbord = new_neighbord.intersection(set([*G.neighbors(old)]))

        if (to_Node in new_neighbord): print(type(old),to_Node); return
        

    
