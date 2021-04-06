
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
    if len(pin)!=4 or any(not(i.isdigit()) for i in pin):
        return "Invalid input."
    return [moves[(int(j)+i)%10] for i,j in enumerate(pin)]

