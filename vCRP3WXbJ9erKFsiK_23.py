
def dif_ciph(decrypt):
    coded = []
    count = 0
    if type(decrypt) == list:
        for index in range(0,len(decrypt)):
            if index == 0:
                coded.append(chr(decrypt[index]))
                count += decrypt[index]
            if index != 0:
                asc = decrypt[index] + count
                coded.append(chr(asc))
                count = asc
        return "".join(coded)
    if type(decrypt) == str:
        for index in range(0,len(decrypt)):
            if index == 0:
                coded.append(ord(decrypt[index]))
            if index != 0:
                asc = ord(decrypt[index]) - ord(decrypt[index-1])
                coded.append(asc)
            
        return coded

