
import numpy as np
​
def isWordChain(words):
    last = np.array([ord(c) for c in words[0]])
    for i in range(1,len(words)):
        current = np.array([ord(c) for c in words[i]])
        if abs(len(current)-len(last))>1: return False
        elif abs(len(current)-len(last)) == 0:
            xor_0 = (last-current != 0)
            if np.sum(xor_0) > 1: return False
        else:
            longer = current if len(current)>len(last) else last
            shorter = last if len(current)>len(last) else current
            xor_start = (longer[:-1]-shorter == 0)
            xor_end = (longer[1:]-shorter == 0)
            xor = np.logical_or(xor_start, xor_end)
            if np.sum(xor) != len(xor): return False
        last = current
    return True

