
def color_conversion(h):
    conversion = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11,
                  "c": 12, "d": 13, "e": 14, "f": 15}
    inv_conversion = {v: k for k, v in conversion.items()}
    if type(h) == str:
        avail_chars = ["#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        valid = True
        for x in h:
            valid = valid and (x in avail_chars)
​
        if valid:
            if len(h) == 6:
                r = 16 * conversion[h[0]] + conversion[h[1]]
                g = 16 * conversion[h[2]] + conversion[h[3]]
                b = 16 * conversion[h[4]] + conversion[h[5]]
​
                return {"r": r, "g": g, "b": b}
            elif len(h) == 7 and h[0] == "#":
                r = 16 * conversion[h[1]] + conversion[h[2]]
                g = 16 * conversion[h[3]] + conversion[h[4]]
                b = 16 * conversion[h[5]] + conversion[h[6]]
​
                return {"r": r, "g": g, "b": b}
            else:
                return "Invalid input!"
        else:
            return "Invalid input!"
    elif type(h) == dict:
        r = h["r"]
        g = h["g"]
        b = h["b"]
​
        string = "#"
​
        if r >= 0 and g >= 0 and b >= 0:
            if r <= 255 and g <= 255 and b <= 255:
                string = string + inv_conversion[(r - r%16) / 16] + inv_conversion[r%16]
                string = string + inv_conversion[(g - g%16) / 16] + inv_conversion[g%16]
                string = string + inv_conversion[(b - b % 16) / 16] + inv_conversion[b % 16]
                return string
            else:
                return "Invalid input!"
        else:
            return "Invalid input!"
    else:
        return "Invalid input!"

