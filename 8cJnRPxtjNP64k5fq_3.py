
def dance(lst, parameter):
    dnc = []
    wom = [x for y in lst for x in y][0::2]
    men = [x for y in lst for x in y][1::2]
    if parameter == 'men':
        dnc = list(zip(wom, men[::-1]))
    elif parameter == 'women':
        dnc = zip(wom[::-1], men)
    return [list(x) for x in dnc]

