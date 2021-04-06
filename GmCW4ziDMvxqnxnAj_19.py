
def who_passed(students):
    result = ' '.join([' '.join([a for b in students[a] if b.split('/')[0] == b.split('/')[1]])  for a in students])
    return sorted([a for a in students if len(students[a]) == result.count(a)])

