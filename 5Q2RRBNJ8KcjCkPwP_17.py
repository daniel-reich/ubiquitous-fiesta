
def tic_tac_toe(inputs):
    a = check(inputs)
    b = check(zip(*inputs))
    c = [[inputs[i][i] for i in range(3)], [inputs[i][2 - i]for i in range(3)]]
    c = check(c)  
    return a or b or c or "It's a Tie"
    
def check(x):
    for i in x:
        if len(set(i)) == 1:
            return "Player {} wins".format(["2", "1"][set(i) == {"X"}])
    return ""

