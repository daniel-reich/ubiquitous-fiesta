
def make_change(c):
    penny,nickle,dime,quarter = 0,0,0,0
    change_dict={}
    while c > 0:
        if c >= 25:
            c -= 25
            quarter +=1
        elif c >= 10:
            c -= 10
            dime +=1
        elif c >=5:
            c -=5
            nickle +=1
        else:
            c -= 1
            penny +=1
    return {"q":quarter, 'd':dime, 'n':nickle, 'p':penny}

