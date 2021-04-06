
def percentage_changed(old, new):
    old, new = int(old[1:]), int(new[1:])
    return '{:.0%} {}'.format(abs(old-new)/old, 'increase' if new > old else 'decrease')

