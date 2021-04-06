
from math import ceil
def spartans_cipher(message, n_Slide):
    if not message:
        return ''
    length = ceil(len(message) / n_Slide)
    message += ' ' * ((length * n_Slide) - len(message)) 
    arr = [[] for i in range(n_Slide)]
    row = 0
    for i,j in enumerate(message):
        if i != 0:
            if i % length == 0:
                row += 1
        arr[row].append(j)
    temp = list(map(list,zip(*arr)))
    ans = ''.join([i for j in temp for i in j])
    while ans[-1] == ' ':
        ans = ans[:-1]  
    return ans

