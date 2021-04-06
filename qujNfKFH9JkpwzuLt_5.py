
def first_index(hex_txt, needle):
    """Find the index of the string needle in the hex text"""
   
    hex_needle = ' '.join(hex(ord(x))[2:] for x in needle)
    # divide by 3 because each hex representation consists of two characters and there is a space between characters
    return hex_txt.find(hex_needle) // 3

