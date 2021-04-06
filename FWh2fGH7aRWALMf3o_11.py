
def cleave(text, lst):
    
    if text in lst:
        return text
    
    found = False
    for word in lst:
        if text.find(word) == 0:
            w_len = len(word)
            sub_result = cleave(text[w_len:], lst)
            if sub_result != "Cleaving stalled: Word not found":
                return word + " " + sub_result
    
    return "Cleaving stalled: Word not found"

