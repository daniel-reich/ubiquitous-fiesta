
def flip_end_chars(string):
    if len(string) < 2 or type(string) != str:
        return "Incompatible."
    elif string[0] == string[-1]:
        return "Two's a pair."
    else:
        return string[-1] + string[1:-1] + string[0]

