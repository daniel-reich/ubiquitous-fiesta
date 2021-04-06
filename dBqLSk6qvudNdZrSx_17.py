
def is_boiling(temp):
    if 'F' in temp: return int(temp.replace('F', '')) >= 212 
    return int(temp.replace('C', '')) >= 100

