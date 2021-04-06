
def track_robot(instructions):
    instructions = ' '.join(instructions)
    new_instructions = instructions.split()
​
    digit_list = [int(d) for d in new_instructions if d.isdigit()]
    instruction_list = [i for i in new_instructions if not i.isdigit()]
​
    dicto = {'right':0,'up':0,'left':0,'down':0}
    for inst,dig in zip(instruction_list,digit_list):
            if inst in dicto:
                dicto[inst] += dig
            else:
                dicto[inst] == 0
​
    return [dicto.get('right') - dicto.get('left'), dicto.get('up') - dicto.get('down')]

