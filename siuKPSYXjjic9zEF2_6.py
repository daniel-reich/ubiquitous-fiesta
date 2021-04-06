
def foil(length):
    import math
    foilThickness = 0.0025
    tubeDiameter = 4.0000
    circumference = math.pi*tubeDiameter
    while length > 0:
        if length >= circumference/2:
            tubeDiameter += foilThickness*2
        else:
            tubeDiameter += foilThickness
        length-=circumference
        circumference = math.pi*tubeDiameter
    return round(circumference/math.pi, 4)

