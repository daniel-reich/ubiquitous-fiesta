
def temp_conversion(celsius):
    f = (celsius*(9/5)) +32
    k = celsius + 273.15
    if k < 0:
        return "Invalid"
    return [round(f, 2), round(k, 2)]

