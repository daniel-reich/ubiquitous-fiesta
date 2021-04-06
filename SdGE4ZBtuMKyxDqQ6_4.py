
def first_repeat(chars):
    for index,val in enumerate(list(chars)):
        if val in list(chars)[index+1:]:
            return val
    
    return '-1'

