
def jumping_frog(n, stones):
    if n < 2:
        return None
    jmpCount = 1 # one jump from the left bank to 1st element
    i = 0
    while i < (n - 1): # visit each stone except the last, (n-1) is the last stone
        distanceToEnd = (n - 1) - i
        jmpValue = stones[i]
        #can we jump ahead? i.e (is there a distance to last stone)
        if 0 < jmpValue <= distanceToEnd:
            # check if we can jump backward ("we did'n reach left bank")
            if (i - jmpValue) >= 0 and stones[i - jmpValue] - 2 * jmpValue > stones[i + jmpValue]:
                i -= jmpValue
            else:
                i += jmpValue
            # increase jump counter
            jmpCount += 1
            # if distance == 0, we reached the end
            if (n - 1) - i == 0:
                return jmpCount + 1
        elif 0 < jmpValue > distanceToEnd: #if stone has abig num to cross the right bank
            return jmpCount + 1
        elif jmpValue == 0 and distanceToEnd > 0: #if we got stuck on a zero num before the end 
            return "no chance :-("

