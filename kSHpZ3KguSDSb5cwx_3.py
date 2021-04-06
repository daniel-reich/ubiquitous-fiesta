
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
    if len(pin)==4 and all([i.isdigit() for i in pin]):
        lst = []
        for i,j in enumerate(pin):
            if int(j)+i >= len(moves):
                lst.append(moves[(int(j)+i)-10])
            else:
                lst.append(moves[int(j)+i])
        return lst
    else:
        return "Invalid input."

