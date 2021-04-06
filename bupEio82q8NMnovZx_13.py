
def track_robot(instructions):
    x = 0
    y = 0
    result = [0,0]
    for i in range(len(instructions)):
        if instructions[i].split()[0] == 'right':
            x=x+int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'left':
            x=x-int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'up':
            y=y+int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'down':
            y=y-int(instructions[i].split()[1])
    return [x,y]

