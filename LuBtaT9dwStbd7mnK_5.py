
def tallest_building_height(height):
    counter = 0 
    for i in height:
        if "#" in i:
            counter +=1
    new = counter * 20
    new = str(new) + "m"
    return new

