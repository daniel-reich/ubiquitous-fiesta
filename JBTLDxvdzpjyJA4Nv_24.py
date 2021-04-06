
def super_reduced_string(txt):
    while True:
        if txt == "":
            return "Empty String"
        else:
            counter = 0
            for i in txt:
                if i*2 in txt:
                    txt = txt.replace(i*2, "")
                else:
                    counter += 1
            if counter == len(txt):
                return txt

