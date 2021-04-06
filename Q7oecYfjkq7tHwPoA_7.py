
import math
def climb(stamina, obstacles):
    j=0
    while (( stamina>0) and  (j<len(obstacles)-1)):
        if obstacles[j]>obstacles[j+1]:
            stamina=stamina- math.ceil(obstacles[j]-obstacles[j+1])
        else:
            stamina = stamina - 2*math.ceil(abs(obstacles[j] - obstacles[j + 1]))
        j += 1
    if stamina<0:
        j-=1
    return j

