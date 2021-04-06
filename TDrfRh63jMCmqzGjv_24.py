
def is_anti_list(lst1, lst2):
    if list(set(lst1)) == list(set(lst2)) :
        for i in range(len(lst1)) :
            if( lst1[i]  ==  lst2[i] ):
                return False
        return True
    else: 
        return False

