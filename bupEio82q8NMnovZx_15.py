
def track_robot(instructions):
    horizontal_movement = 0
    vertical_movement = 0
    final_instructions = []
    for element in instructions:
        specific_instructions = element.split()
        if specific_instructions[0] == 'right':
            horizontal_movement += int(specific_instructions[1])
        elif specific_instructions[0] == 'left':
            horizontal_movement -= int(specific_instructions[1])
        elif specific_instructions[0] == 'up':
            vertical_movement += int(specific_instructions[1])
        else:
            vertical_movement -= int(specific_instructions[1])
    final_instructions.append(horizontal_movement)
    final_instructions.append(vertical_movement)
    return final_instructions

