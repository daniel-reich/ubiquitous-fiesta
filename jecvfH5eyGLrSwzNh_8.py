
def fauna_number(s):
    '''
    Returns a list of tuples (animal, n) where animal is present in Chitwan
    National Park and n is the number of this animal in s.
    '''
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth",
               "monitorlizard", "bengaltiger"]
    s = s.replace(',',' ').replace('.',' ').split()
    
    return [(animal, s[i-1]) for i, animal in enumerate(s)
            if animal in animals]

