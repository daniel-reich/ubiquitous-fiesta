
def series_resistance(lst):
    a = sum(lst)
    if a > 1:
        return str(a) + ' ohms'
    else:
        return str(a) + ' ohm'

