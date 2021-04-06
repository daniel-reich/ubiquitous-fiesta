
import math
def climb (stamina , obstacles):
    trials = 0
    while len(obstacles) > 1 :
        distance = 2 * (math.ceil(abs((obstacles[1] - obstacles[0])))) if (obstacles[1] - obstacles[0]) > 0 else math.ceil(abs((obstacles[1] - obstacles[0])))
        if stamina - distance < 0 :
            break
        else : 
            stamina = stamina - distance
            trials += 1 
            obstacles.pop(0)
            
        
    return trials

