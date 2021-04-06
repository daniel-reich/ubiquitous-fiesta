
def zip_it(women,men):
    if len(women)==len(men):
        return [((a,)+(b,)) for a,b in zip(women,men) ]
    else:
        return "sizes don't match"

