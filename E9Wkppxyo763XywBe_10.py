
def binary_clock(time):
    clock = 4*[""]
    format = [2,4,3,4,3,4]
    time = time.replace(':', '')
    for i in range(len(time)):
        binary = ' ' * (4-format[i]) + ('{0:0' + str(format[i]) + 'b}').format(int(time[i]))
        for j in range(len(binary)):
            clock[j] += binary[j]
​
    return clock

