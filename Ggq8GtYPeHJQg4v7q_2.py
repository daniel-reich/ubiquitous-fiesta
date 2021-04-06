
def replace_vowels(txt, ch):
    
    for char in txt:
        
        if char in "aeiou":
            
            txt = txt.replace(char,ch)
            
    return txt

