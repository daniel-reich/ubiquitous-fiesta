
def number_length(num):
    num = str(num)
    if num == "":
        return 0
    else:
        return 1 + number_length(num[:-1])

