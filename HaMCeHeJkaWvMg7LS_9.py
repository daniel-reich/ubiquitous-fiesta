
def sun_loungers(beach):
    count, last = 0, True
    nex = beach[0] == "0"
    for i in range(len(beach)-1):
        if nex:
            nex = beach[i + 1] == "0"
            if last and nex:
                count += 1
                last = False
            else:
                last = True
        else:
            nex = beach[i + 1] == "0"
            last = False
    return count + (last*(beach[-1] == "0"))

