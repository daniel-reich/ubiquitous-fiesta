
def staircase(num):
    stairs = ""
    if num > 0:
        for i in range(1, num):
            stairs += "_" * (num - i)
            stairs += "#" * i
            stairs += "\n"
        stairs += "#" * num
    else:
        num_abs = -num
        for i in range(1, num_abs):
            stairs += "_" * (i-1)
            stairs += "#" * (num_abs + 1 - i)
            stairs += "\n"
        stairs += "_" * (num_abs - 1)
        stairs += "#"
    return stairs

