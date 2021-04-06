
def wrap_around(string, offset):
    
    numeral = offset%len(string)
    
    return string[numeral:len(string)]+string[:numeral]

