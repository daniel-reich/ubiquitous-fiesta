
def construct_fence(p):
    cost=int(p[1:].replace(",",""))
    Million=1000000
    fenceLength=int(Million/cost)
    the_fence=""
    for fence in range(fenceLength):
        the_fence+="H"
    return the_fence

