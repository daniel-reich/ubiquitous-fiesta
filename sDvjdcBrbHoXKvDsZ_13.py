
def anagram(name, *words):
    
    b = "".join(list(words[0]))
    c = "".join(name)    
    if sorted(b.lower()) == sorted(c.lower())[1:]:
        return True
    return False

