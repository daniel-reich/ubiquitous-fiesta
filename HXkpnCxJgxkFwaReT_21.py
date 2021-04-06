
def count_datatypes(*args):
​
    lst_1 = [0, 0, 0, 0, 0, 0]
​
    for i in args:
        if type(i) == int:
            lst_1[0] += 1
        elif type(i) == str:
            lst_1[1] += 1
        elif type(i) == bool:
            lst_1[2] += 1
        elif type(i) == list:
            lst_1[3] += 1
        elif type(i) == tuple:
            lst_1[4] += 1
        elif type(i) == dict:
            lst_1[5] += 1
        
    return lst_1

