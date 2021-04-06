
def validate_swaps(lst, txt):
    a = []
    for word in lst:
        
        word = list(word)
​
        if len(word) != len(txt):
            a.append(False)
            continue
        
        for letter in word:
            your_letter = word.index(letter)
            belongs = txt.find(letter)
            
            if your_letter != belongs:
                break
        
        if belongs < 0:
            a.append(False)
            continue
​
        word[your_letter], word[belongs] = word[belongs], word[your_letter]
​
        if word == list(txt):
            a.append(True)
        else:
            a.append(False)
    
    return a

