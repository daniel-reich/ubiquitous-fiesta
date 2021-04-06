
def hex_color_mixer(cs):
    '''
    Returns the rgb hex string representing the colour made by averaging the red,
    green and blue values of each colour c in cs as discussed above
    '''
    c_vals = [[int(c[i:i+2],16) for i in range(1,7,2)] for c in cs]
    return '#' + ''.join(hex(int(sum(hue)/len(hue)+.5)).upper()[2:].zfill(2) \
                         for hue in zip(*c_vals))

