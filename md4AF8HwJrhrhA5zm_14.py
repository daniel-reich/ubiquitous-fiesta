
from collections import OrderedDict 
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    comb=('complementary','analogous','triadic','split_complementary','rectangle','square')
    pos=((12,6),(12,1,11),(12,4,8),(12,5,7),(12,2,6,8),(12,3,6,9))
    sel=OrderedDict.fromkeys(comb)
    k=0
    for i in sel.keys():
        sel.update({i:pos[k]})
        k+=1
    p=sel.get(combination)
    return set([colours[(colours.index(anchor)+x)%12] for x in p])

