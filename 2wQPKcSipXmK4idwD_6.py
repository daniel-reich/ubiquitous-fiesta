
def find_it(items, name):
    try:
        i = items[name]
        return '{} is gone...'.format(name.title())
    except KeyError:
        return '{} is here!'.format(name.title())

