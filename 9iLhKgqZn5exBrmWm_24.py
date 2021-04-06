
def ascending(txt):
    for i in range(2,len(txt)+1):
        if len(txt) % i == 0:
            digits = int(len(txt)/i)
            for index in range(0, len(txt)-digits, digits):
                if int(txt[ index : index + digits]) == int(txt[ index + digits : index + (digits*2)]) - 1:
                    if index == len(txt)-(digits*2): return True
                else: break
    return False

