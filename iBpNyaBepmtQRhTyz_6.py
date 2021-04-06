
import numpy as np
​
​
def c_cipher(msg, keyword):
    new_msg = ''
    
    if ' ' in msg:
        msg = [ch.lower() for ch in msg if ch.isalpha() or ch.isdecimal()]
        
        missing = len(msg) % len(keyword)
        if missing:
            for _ in range(len(keyword) - missing):
                msg.append('x')
        
        dim = len(msg) // len(keyword)
        arr = np.asarray(msg).reshape(dim, len(keyword))
        
        for ch in sorted(keyword):
            i = keyword.index(ch)
            new_msg += ''.join(arr[:, i])
    else:
        dim = len(msg) // len(keyword)
        arr = np.asarray(list(msg)).reshape((len(keyword), dim))
        
        for j in range(dim):
            for ch in keyword:
                i = sorted(keyword).index(ch)
                new_msg += arr[i, j]
    
    return new_msg

