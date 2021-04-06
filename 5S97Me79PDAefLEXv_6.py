
def lambda_to_def(code):
    code=code.split(" ")
    for index, i in enumerate(code):
        if i[-1]==":" :
            g=index
    if int(g)==3:
        gen = code[g]
        kew=int(len(gen)-1)
        gen= gen[:kew]
        vr ="def"+" "+ code[0] + "(" + gen + ")"
    else:
        cod=code[3:int(g)]
        cod=" ".join(cod)
        gen = code[g]
        kew = int(len(gen) - 1)
        gen = gen[:kew]
        vr="def"+" "+code[0]+"("+cod+" "+gen+")"
    f = code[int(g) + 1:]
    f = " ".join(f)
    f=":\n\treturn"+" "+f
    final=vr+f
    return(final)

