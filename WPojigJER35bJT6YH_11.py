
def reversed_binary_integer(num):
    output = 0
    power = 0
    for i in bin(num)[2:]:
        output += 2**power*int(i)
        power += 1
    return output

