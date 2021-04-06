
def find_nemo(string):
    ind = ""
    splitted = str(string).split(" ")
​
    if "Nemo" in splitted:
        ind= splitted.index("Nemo")
        return "I found Nemo at {}!".format(ind+1)
    else:
        return "I can't find Nemo :("

