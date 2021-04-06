
def hamming_code(message):
    list = []
    hamming = ""
    for i in range(len(message)):
        list.append(bin(ord(message[i]))[2:].zfill(8))
    for i in range(len(list)):
        for j in range(8):
            hamming = hamming+str(list[i][j])+str(list[i][j])+str(list[i][j])
    return hamming

