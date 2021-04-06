
def inverter(txt, type):
    conversion = {'P': ' '.join(txt.split()[::-1]).capitalize(),
                  'W': ' '.join([w[::-1] for w in txt.split()]).capitalize()}
    return conversion[type]

