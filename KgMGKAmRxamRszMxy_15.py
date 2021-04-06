
def spartans_cipher(message, n_Slide):
    
    import math
    
    result_lst = []
    
    Slide2 = math.ceil(len(message) / n_Slide)
    
    for i in range(0, Slide2):
        for j in range(0, n_Slide):
            if Slide2 * j + i < len(message):
                result_lst.append(message[Slide2 * j + i])
            else:
                result_lst.append(' ')
    
    if len(result_lst) > 0:
        while result_lst[-1] == ' ':
            del result_lst[-1]
    else:
        pass
    
    return ''.join(result_lst)

