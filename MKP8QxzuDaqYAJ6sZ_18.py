
def is_correct_aliases(names, aliases):                                         
    aliases = [alias[0] for alias in aliases if alias.split()[0][0] == alias.split()[1][0]]
    for name in names:                                                          
        if name[0] in aliases:                                                  
            aliases.remove(name[0])                                             
        else:                                                                   
            return False                                                        
    return not bool(aliases)

