
def double_letters(word):
    a=0
    for x in range(0,len(word)):
        if x>0:
            if word[x]==word[x-1]:
                a=a+1
    return a>0

