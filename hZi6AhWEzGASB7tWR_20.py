
def check(lst):
    if all(x<y for x, y in zip(lst, lst[1:])) == True:
       return 'increasing'
    elif len(set(lst)) != len(lst):
       return 'neither'
    else:
       return 'decreasing'

