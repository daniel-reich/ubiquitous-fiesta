
def flatten(lst):
    return eval("[" + str(lst).replace("[", "").replace("]", "") + "]")
def count_number(lst):
    return len(list(filter(lambda x:type(x)!=type('1'),flatten(lst))))

