
def wiggle_string(s):
    return [' '*l+s for l in range(0,len(s)+1)]+ [' '*l+s for l in range(len(s)-1,-1,-1)]

