
def power_morphic(num):
    dic = {0:"Amorphic", 1:"Enamorphic", 2:"Dimorphic", 4:"Quadrimorphic", 9:"Polymorphic"}
    return dic[sum(str(num**k)[-len(str(num)):]==str(num) for k in range(2,11))]

