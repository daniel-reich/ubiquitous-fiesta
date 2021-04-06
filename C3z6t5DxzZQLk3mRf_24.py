
def tune(lst):
    matches = [329.63, 246.94, 196, 146.83, 110, 82.41]
​
    result = []
    for f, l in zip(matches, lst):
        if l == 0:
            result.append(' - ')
        else:
            diff = round((f - l) / l * 100)
            if diff == 0:
                result.append('OK')
            elif diff < -2:
                result.append('+<<')
            elif diff in (-1, -2):
                result.append('+<')
            elif diff > 2:
                result.append('>>+')
            elif diff in (1, 2):
                result.append('>+')
    return result

