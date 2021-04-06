
import math
def hex_color_mixer(colors):
    def hex_to_rgb(value):
        value = value.lstrip('#')
        return list(int(value[i:i + 2], 16) for i in (0, 2, 4))
    def normal_round(n):
        if n - math.floor(n) < 0.5:
            return math.floor(n)
        return math.ceil(n)
    lst = []
    for i in colors:
        lst.append(hex_to_rgb(i))
    cum_lst = list(map(sum, zip(*lst)))
    return '#%02X%02X%02X' %  tuple([normal_round(i/len(colors)) for i in cum_lst])

