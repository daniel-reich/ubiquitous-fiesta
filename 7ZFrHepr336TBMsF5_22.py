
def percentage_changed(old, new):
    num = 1 - (int(new.replace('$','')) / int(old.replace('$','')))
    return '{}% {}'.format(abs(int(num * 100)), 'increase' if num < 0 else 'decrease')

