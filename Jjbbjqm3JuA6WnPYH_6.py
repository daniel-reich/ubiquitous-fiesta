
def bit_rotate(n, m, d):
    # Get binary values (as string)
    binary = str(bin(n))[2:]
    # Get the new indexes: take into account if d = True or False
    indexes = [i%len(binary) for i in range(-len(binary)-m, 0-m)] if d else [i%len(binary) for i in range(0+m, len(binary)+m)] 
    # Make the new rotated binary value based on the indexes
    rotated = "".join([str(binary[i]) for i in indexes])
    
    return int(rotated, 2)

