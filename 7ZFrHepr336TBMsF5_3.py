
def percentage_changed(old, new):
    diff = (int(new[1:]) - int(old[1:])) / int(old[1:])
    return '{}% {}crease'.format(abs(round(diff * 100)),
                                 'in' if diff > 0 else 'de')

