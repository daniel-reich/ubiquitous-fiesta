
def is_heteromecic(num):
    heteromecic = None
    if(num == 0):
        heteromecic = True
    for val in range(0,num):
        if(val*(val +1) == num):
            
            heteromecic = True
            break
        else: heteromecic = False
    return heteromecic

