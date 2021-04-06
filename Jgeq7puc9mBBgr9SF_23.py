
def complete_binary(s):
    if len(s)%8!=0:
        while len(s)%8!=0:
            s="0"+s
        return s
    else:
        return s

