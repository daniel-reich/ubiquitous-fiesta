
def get_length(lst):
    lst=str(lst)
    a=lst.strip('[]')
    x=[i for i in a if i.isdigit()]
    return len(x)

