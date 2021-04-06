
def free_throws(success, rows):
    return '{}%'.format(round((float(success[:-1]) / 100) ** rows * 100))

