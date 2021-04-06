
import re
def swap_xy(txt):
    result = [int(i) for i in re.findall(r'-?\d+', txt)]
    print(result)
    for i in range(len(result)):
        if i%2 == 0:
            result[i], result[i+1] = result[i+1], result[i]
    return "("+str(result[0])+", "+str(result[1])+"), ("+str(result[2])+", "+str(result[3])+")"

