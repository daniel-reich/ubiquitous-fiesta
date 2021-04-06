
def valid_color(color):
    alpha = False
    percentage = False
    color = color.split('(')
    rg = color[0]
    if ' ' in rg: return False
    value = (color[1])[:-1].split(',')
    value = list(filter(lambda x: x != '', value))
    if rg == 'rgba': alpha = True
    if rg == 'rgb' and len(value) != 3 or rg == 'rgba' and len(value) != 4: return False
    for k,i in enumerate(value):
        if '%' in i:
            i = i.replace('%', '')
            percentage = True
        try:
            ans = int(i)
        except:
            ans = float(i)
        if (percentage and (ans < 0 or ans > 100)) or (not percentage and (ans < 0 or ans > 255)) or (alpha and k == 3 and (ans < 0 or ans > 1)): return False
    return True

