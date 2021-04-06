
def chunkify(lst, size):
    new_lst = []
    for i in range(0,len(lst), size):
        try:
            new_lst.append(lst[i:i+size])
        except IndexError:
            new_lst.append(lst[i:])
    return new_lst

