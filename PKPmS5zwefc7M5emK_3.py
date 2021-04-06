
def missing_angle(a,b):
    return 'obtuse' if 180-(a+b)>90 else 'right' if 180-(a+b)==90 else 'acute'

