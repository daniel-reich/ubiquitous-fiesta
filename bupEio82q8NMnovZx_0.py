
def track_robot(instructions):
    totals = {'left':0, 'right':0, 'up':0, 'down':0}
    for step in instructions:
        step = step.split()
        totals[step[0]] += int(step[1])
    return [totals['right'] - totals['left'], totals['up'] - totals['down']]

