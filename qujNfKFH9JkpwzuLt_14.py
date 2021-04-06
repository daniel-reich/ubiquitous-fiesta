
def first_index(hex_txt, needle):
    
    neddleChars = list(needle)
    charsNeedle = list(map(lambda x: x[2:], list(map(lambda x: hex(ord(x)), neddleChars))))
    
    hex_txtList = hex_txt.split(" ")
    
    #print(hex_txtList)
    
    for char in charsNeedle:
        for idx in range(len(hex_txtList)):
            if char == hex_txtList[idx]:
                return idx

