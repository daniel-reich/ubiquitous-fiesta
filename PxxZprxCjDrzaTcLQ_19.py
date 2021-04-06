
def vowel_links(txt):
    
    txt = txt.split()
​
    for i in range(len(txt)-1):
​
        if txt[i][-1] in 'aeiou' and txt[i+1][0] in 'aeiou':
            return True
    return False

