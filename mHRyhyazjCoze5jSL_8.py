
def double_swap(string,chr1,chr2):
    new_string = ""
    for char in string:
        if char == chr1:
            new_string = new_string + chr2
        elif char == chr2:
            new_string = new_string + chr1
        else:
            new_string = new_string + char
    return new_string

