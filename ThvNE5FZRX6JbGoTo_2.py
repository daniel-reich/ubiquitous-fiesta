
def inverter(txt, type):
    if type == 'P':
        return ' '.join([i for i in txt.split()][::-1]).capitalize()
    return ' '.join(i[::-1] for i in txt.split()).capitalize()

