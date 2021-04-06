
def lost_dog(*args):
    dogs,j={},0
    for i,v in enumerate(args):
        if 0 in v:
            j+=1
            dogs["Dog"+str(j)] = "House ({}) and Room ({})".format(i+1,v.index(0)+1)
    return dogs if len(dogs)!=0 else "Dog not found!"

