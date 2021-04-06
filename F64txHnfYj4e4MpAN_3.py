
def schoty(frame):
    current = 1000000
    output = 0
    for i in frame:
        output += len(i.split("-")[0])*current
        current//=10
    return output

