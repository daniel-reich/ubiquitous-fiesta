
def column_chart(productA, productB, target):
    import numpy as np
    prodA = list(map(lambda x:x//10,productA))
    prodB = list(map(lambda x:x//10,productB))
    tar = list(map(lambda x:x//10,target))
    
    prodAandB = list(map(sum,zip(prodA,prodB)))
    
    maxheight = max(tar)+1
​
    grid2 = [['++' if col < prodA[day] else '**' if col < prodAandB[day] else '__' if col == tar[day] else '  ' for day in range(7)] for col in range(maxheight)][::-1]
    
    s = ''
    for row in range(maxheight):
        r = '{} | '.format((maxheight-row)*10) + ' '.join(grid2[row]) + ' |\n'
        s += r
    
    s += '   | Mo Tu We Th Fr Sa Su |'
    
    return s

