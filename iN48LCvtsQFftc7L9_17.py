
import numpy as np
​
def word_search(letters, words):
    arr = np.array(list(letters.lower())).reshape((8, 8))
​
    lines = []
    for i in arr:
        lines.append(''.join(i))
    for i in range(-5, 6):
        lines.append(''.join(np.diag(arr, i)))
    arr = np.rot90(arr)
    for i in arr:
        lines.append(''.join(i))
    for i in range(-5, 6):
        lines.append(''.join(np.diag(arr, i)))
        
    for word in words:
        if not any(word in i for i in lines) and not any(word[::-1] in i for i in lines):
            return False
    return True

