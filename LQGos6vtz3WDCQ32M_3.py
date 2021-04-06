
def Kaprekar(n):
    if len(set(str(n))) == 1 and n > 9:
        m = "\n---------- The Mysterious Number 6174 ----------\n"
        m2 = "\nError, n cannot be a repdigit.\n"
        m3 = "\n------------------------------------------------"
        return m + m2 + m3
    i = 0
    message2 = ""
    while n != 6174:
        i += 1
        small = "".join(sorted(str(n)))
        big = ("".join(sorted(str(n), reverse=True)))
        while len(big) < 4:
            big += "0"
        n = int(big) - int(small)
        message2 += "Iteration Nr. {}: {} - {} = {}\n".format(i, big, small.zfill(4), str(n).zfill(4))
        
    message1 = "\n---------- The Mysterious Number 6174 ----------\n"  
    message1 += "\nNumber of iterations: {}\n".format(i) 
    message1 += "\nIterations:\n\n"
    message3 = "\n------------------------------------------------"
    return message1 + message2 + message3

