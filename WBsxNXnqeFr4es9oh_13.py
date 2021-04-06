
import math
​
def clockwise_cipher(message):
    width = math.ceil(math.sqrt(len(message)))
    table = [[None for _ in range(width)] for _ in range(width)]
    msg = message + ' ' * (width**2 - len(message))
    
    w = width
    width -= 1
    index = 0
    b = 0
    while width > 0:
        for i in range(width):
            table[b][b+i] = msg[index]
            table[b+i][w-1-b] = msg[index + 1]
            table[w-1-b][w-1-b-i] = msg[index + 2]
            table[w-1-b-i][b] = msg[index + 3]
            index += 4
        b += 1
        width -= 2
    if width == 0:
        center = math.floor(w/2)
        table[center][center] = msg[-1]
        
    result = ''
    for row in table:
        for val in row:
            result += val
    return result

