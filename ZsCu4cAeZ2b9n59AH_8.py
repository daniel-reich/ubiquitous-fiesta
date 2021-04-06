
def lost_dog(*houses):
    ans = {}
    k = 0
    dogs = 0
    for house in houses:
        k += 1
        if 0 in house:
            dogs += 1
            ans["Dog" + str(dogs)] = "House (" + str(k) + ") and Room (" + str(house.index(0) + 1) + ")"        
    return ans if len(ans.keys()) > 0 else "Dog not found!"

