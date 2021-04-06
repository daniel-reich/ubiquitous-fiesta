
def is_rectangle(coordinates):
    if len(coordinates) != 4 or len(removeDuplicates(coordinates)) != 4:
        return False
    
    flag = 1
    for elem in coordinates:
        lst = coordinates
        coords = elem.split(",")
        lst.remove(elem)
        for i in lst:
            if str(coords[0]) in i and str(coords[0]) in i:
                flag = 0
​
    if flag == 1:
        return  False
    return True 
​
​
def removeDuplicates(txt):
    letters = []
    [letters.append(l) for l in txt if l not in letters]
    return letters

