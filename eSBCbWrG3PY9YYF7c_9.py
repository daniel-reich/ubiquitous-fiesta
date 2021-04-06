
def sexagenary(yr):
    stems = ['Wood','Wood','Fire','Fire','Earth','Earth','Metal','Metal','Water','Water']
    branches = ['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep','Monkey','Rooster','Dog','Pig']
    stems += stems*5
    branches += branches*4
    cycle = [i+' '+j for i,j in zip(stems,branches)]
    index = (yr-1984)%60
    return cycle[index]

