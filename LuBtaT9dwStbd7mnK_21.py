
def tallest_building_height(lst):
    INCREMENTS = 20
    LEGEND = "#"
    totalHeight = 0
​
    nRows = len(lst)
​
    legends = 0
​
    for i in range(nRows):
        layer = lst[i]
​
        for block in layer:
            if(block == LEGEND):
                legends += 1 #otherwise, it's plain skyline
                break
​
    print("FOUND ", legends, " LEGENDS")
    
    
    totalHeight = legends * INCREMENTS
    heightString = str(totalHeight) + "m"
    print("TOTAL HEIGHT: ", heightString)
​
    return heightString

