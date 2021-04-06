
def percent_filled(box):
    string = (''.join(box)).replace('#', '')
    return str(int(string.count('o') / len(string) * 100)) + '%'

