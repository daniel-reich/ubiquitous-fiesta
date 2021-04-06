
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
    if not pin.isdigit() or len(pin)<4:
        return "Invalid input."
    else:
        return [moves[(int(num)+i)%len(moves)] for i,num in enumerate(pin)]

