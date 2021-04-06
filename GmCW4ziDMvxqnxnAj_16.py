
def who_passed(students):
    return sorted([s for s in students if all(n == d for n,d in [mark.split('/') for mark in students[s]])])

