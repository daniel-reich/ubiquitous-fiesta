
def isWordChain(words):
    print(words)
    prev = None
    for x in words:
        print(x)
        pointer = x
        spent = False
​
        if prev:
            if prev == pointer: return False
​
            if len(prev) == len(pointer):
                for i, l in enumerate(prev):
                    if pointer[i] != l and not spent:
                        spent = True
                    elif pointer[i] != l and spent:
                        return False
            else:      
            # did you add or subtract
                if len(prev) < len(pointer):
                    w, a = pointer, prev
                if len(prev) > len(pointer):
                    w, a = prev, pointer
​
                for b in a:
                    if b not in w:
                        return False
​
                if len(w) - len(a) != 1: return False
​
​
​
        prev = pointer
    return True

