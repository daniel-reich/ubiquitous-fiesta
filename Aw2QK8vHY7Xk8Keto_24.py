
def longest_word(s):
    max=0
    a=s[0]
    for i in s.split():
        if(len(i)>max):
            max=len(i)
            a=i
    return a

