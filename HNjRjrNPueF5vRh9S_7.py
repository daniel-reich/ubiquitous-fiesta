
def hamming_code(message):
    asciis=[]
    for i in message:
        asciis.append(ord(i))
    
    print(asciis)
    binary=[]
    for i in asciis:
        binary.append('{0:08b}'.format(i))
    
    print(binary)
    last=""
    for i in binary:
        for j in i:
            last+=j*3
    
    return last

