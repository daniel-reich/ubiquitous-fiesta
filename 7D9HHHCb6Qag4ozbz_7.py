
def find_zip(txt):
    Zip = txt.find("zip")
    second_ac = 1
    while Zip != -1:
        second_ac += 1
        Zip = txt.find("zip", Zip + 1)
        index = Zip
        if second_ac == 2:
            return index
        elif second_ac < 2:
            return -1

