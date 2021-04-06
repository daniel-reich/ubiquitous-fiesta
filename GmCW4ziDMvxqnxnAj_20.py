
def who_passed(students):
    return sorted(map(lambda s: s[0], filter(lambda y: all(y[1]),
                                           [(i, map(lambda x: x.split('/')[0] == x.split('/')[1], b)) for i, b in
                                            students.items()])))

