
def flip_end_chars(txt):
    return "Incompatible." if len(txt)<2 or type(txt)!=str else "Two's a pair." if txt[0]==txt[-1] else txt[-1]+txt[1:len(txt)-1]+txt[0]

