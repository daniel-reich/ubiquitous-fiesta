
def text_to_number_binary(txt):
    arr = txt.split(' ')
    
    numList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    s = ''
    for x in arr:
        if x.lower() in ['zero', 'one']:
            s = s + str(numList.index(x.lower()))
        if x.lower() == 'ten':
            s = s + '1'
            
    #print(s)
        
    if len(s) < 8:
        return ''
    if len(s )>8:
        s = s[:len(s) - len(s) % 8]
    return s

