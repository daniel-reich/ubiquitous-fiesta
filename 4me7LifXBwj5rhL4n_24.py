
def circle_or_square(rad, area):
    circum=2*3.14*float(rad)
    side=float(area)**0.5
    peri=4*side
    if circum>peri:
        return True
    else:
        return False

