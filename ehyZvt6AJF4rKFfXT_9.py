
def uncensor(txt, vowels):
    new_txt = ''
    v_list = [v for v in vowels]
    
    for x in txt:
        if x == '*':
            new_txt += v_list.pop(0)
        else:
            new_txt += x
            
    return new_txt

