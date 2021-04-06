
def find_and_remove(dct):
    ans = {i:{key: int(value) for key,value in dct[i].items() if dct[i][key].isnumeric()} for i in dct}
    return ans

