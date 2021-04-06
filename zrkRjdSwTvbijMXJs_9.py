
def encrypt(plncode, pad):
    cypher=""
    # first 5 of pad = keyID
    keyID=pad[0:5]
    # print("keyID",keyID)
     # output starts with keyID
    cypher+=keyID
    # create encrypted code
    for i in range(0,len(plncode)):
        # plncode - pad
        cyp_digit=int(plncode[i])-int(pad[i+5])
        # if neg add 10
        if cyp_digit < 0:
            cyp_digit+=10
        # add to output
        cypher+=str(cyp_digit)
    return cypher
    
def decrypt(cypcode, pad):
    plain=""
    # compare keyID
    cyp_key=cypcode[0:5]
    pad_key=pad[0:5]
    # if no match 
    if cyp_key != pad_key:
        return "Error: Key IDs don't match."
    # plncode + pad
    for i in range(5,len(cypcode)):
        pln_digit=int(cypcode[i])+int(pad[i])
        # if >= 10 substract 10 
        if pln_digit >= 10:
            pln_digit-=10
        # add to output
        plain+=str(pln_digit)    
    return plain

