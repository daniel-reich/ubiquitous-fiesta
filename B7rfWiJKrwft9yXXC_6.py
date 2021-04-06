
def sort_descending(num):
    lst = [i for i in str(num)]
    lst.sort(reverse=True)
    result = ''
    for i in lst:
        result = result + i
    return int(result);

