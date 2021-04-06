
def inverter(txt, type):
    if type == 'P':return ' '.join(txt.split(' ')[::-1]).capitalize()
    return  ' '.join(list(map(lambda x:x[::-1], txt.split(' ')))).capitalize()

