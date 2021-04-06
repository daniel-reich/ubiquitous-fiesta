
def next_letters(s):
    if s == '' :
        return 'A'
    elif s.count('Z') == len(s) :
        return (len(s)+1)*'A'
    else :
        z = 0 # number of z at the end of our string
        while s[::-1][z] == 'Z' : z += 1
        pA, pZ = s[::-1][:z:-1], s[-z-1:] # splitting into 2 parts : constant/changed
        pZ = chr(ord(pZ[0])+1) + (len(pZ)-1)*'A' # changing first value to its next one and Z to As
        return pA + pZ

