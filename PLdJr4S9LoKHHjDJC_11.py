
def identify(*cube):
    x=[0]
    for row in cube:x+=[len(row)]
    for r in x[1:]:x[0]+=max(x[1:])-r
    if x[0]>0: return "Missing "+str(x[0])
    if len(cube)<max(x[1:]): return "Non-Full"
    return "Full"

