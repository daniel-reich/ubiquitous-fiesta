
def decrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    splitter = 0
    hold = ""
    for x in range(len(s)):
        if splitter == x:
            if splitter+2 < len(s):
                if s[splitter+2] == "#":
                    hold += alphabet[int(s[splitter:splitter+2])-1]
                    splitter += 2
                else:
                    hold += alphabet[int(s[splitter])-1]
                splitter += 1
            else:
                hold += alphabet[int(s[splitter])-1]
                splitter += 1
    return hold

