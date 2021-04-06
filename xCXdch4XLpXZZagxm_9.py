
def num_of_leapyears(string):
    counter = 0
    string = string.split("-")
    for i in range(int(string[0]), int(string[1]) + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            counter += 1
    return counter

