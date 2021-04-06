
def sun_loungers(beach):
    if beach == "0":
        return 1
    beach = list(beach)
    counter = 0
    for i in range(0,len(beach)):
        if i == 0:
            if beach[i] == "0" and beach[i+1] == "0":
                counter += 1
                beach[i] = "1"
        elif i == len(beach)-1:
            if beach[i] == "0" and beach[i-1] != "1":
                counter += 1
                beach[i] = "1"
        elif beach[i] == "0" and beach[i-1] == "0" and beach[i+1] == "0":
            counter += 1
            beach[i] = "1"
    return counter

