
def is_repeated(test_str):
    res = None
    temp = (test_str + test_str).find(test_str, 1, -1) 
    if temp != -1: 
        res = test_str[:temp]
        return round(len(test_str)/len(res))
    else: return False

