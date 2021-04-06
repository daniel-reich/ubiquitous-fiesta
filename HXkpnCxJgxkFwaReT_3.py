
def count_datatypes(*args):
    r=[0,0,0,0,0,0]
    for _ in args:
        if type(_) == int:
            r[0] += 1
        elif type(_) == str:
            r[1] += 1
        elif type(_) == bool:
            r[2] += 1
        elif type(_) == list:
            r[3] += 1
        elif type(_) == tuple:
            r[4] += 1
        elif type(_) == dict:
            r[5] += 1
    return(r)

