
def inverter(s, t):
    arr = s.lower().split(' ')
    if t == 'P':
        return ' '.join(arr[::-1]).capitalize()
    return ' '.join(i[::-1] for i in arr).capitalize()

