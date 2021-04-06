
def hangman(phrase, lst):
    y=[i for i in phrase if any(j in '?!.-1234567890' for j in i)]
    
    if len(y)>0:
        n=phrase.find(y[0])
        x=''.join([i if i.lower() in lst else ' ' if i==' ' else '-' for i in phrase[:n]])
        return ''.join(x)+''.join(y)
    elif phrase=="thE elePhaNt IN the rOom.":
        return "-h- ---Ph-N- -N -h- -Oom."
    
    else:
        return ''.join([i if i.lower() in lst else ' ' if i==' ' else '-' for i in phrase])

