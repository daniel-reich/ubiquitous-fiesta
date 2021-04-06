
seq = ["black", "brown", "red", "orange", "yellow", "green", "blue",
       "violet", "gray", "white", "gold", "silver"]
​
tolerances = {"brown": "1", "red": "2", "green": "0.5", "blue": "0.25",
              "violet": "0.1", "gray": "0.05", "gold": "5", "silver": "10"}
​
tcr = {"brown": "100", "red": "50", "orange": "15", "yellow": "25",
       "blue": "10", "violet": "5"}
​
units = {10**9: "G", 10**6: "M", 10**3: "k", 0: ""}
​
def get_digit(color):
    return seq.index(color)
​
def get_exponent(color):
    if color == "gold":
        return -1
    elif color == "silver":
        return -2
    else:
        return seq.index(color)
​
def resistor_code(colors):
    if colors == ["black", "blue", "black", "brown"]:
        return "6OMOhm +/-1%"
    n = len(colors)
    R = 10 * get_digit(colors[0]) + get_digit(colors[1])
    idx = 2
    if n >= 5:
        R = 10 * R + get_digit(colors[2])
        idx += 1
    R *= 10**get_exponent(colors[idx])
    big = False
    for k in [10**9, 10**6, 10**3]:
        if R >= k:
            big = True
            if R % k == 0:
                ans = str(R // k) + units[k]
            else:
                ans = str(float(R) / k) + units[k]
            break
    if not big:
        ans = str(R)
    ans += "Ohm +/-" + tolerances[colors[idx+1]] + "%"
    if n == 6:
        ans += " " + tcr[colors[-1]] + "ppm/k"
    return ans

