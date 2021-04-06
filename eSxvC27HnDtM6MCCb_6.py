
def base_n(base, values, number):
    if len(values) != base:
        return False
    string = ""    
    while number:
        string = str(values[number % base]) + string
        number //= base
    return string

