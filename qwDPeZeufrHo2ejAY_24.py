
def eval_algebra(eq):
    eql= (eq.replace(" ","")).split('=')
    if ("x" in eql[0]):
        if ("+" in eql[0]):
            newl=eql[0].split("+")
            
            return int(eql[1])-int(newl[1]) if newl[0].isalpha() else int(eql[1])-int(newl[0])
        else:
            newl=eql[0].split("-")
            if eql[0].count("-")==2:
                #x is second
                return -int(eql[1])-int(newl[1])
            else:
                return int(eql[1])+int(newl[1]) if "x" in newl[0] else -int(eql[1])+int(newl[0])
    else:
        return eval(eql[0])

