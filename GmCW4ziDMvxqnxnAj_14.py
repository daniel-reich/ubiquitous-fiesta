
def who_passed(students):
    result = []
    lst = []
    
    for name in students:
        for grades in students[name]:
            if eval(grades) == 1:
                lst.append(True)
            else:
                lst.append(False)
        if all(lst):
            result.append(name)
        lst = []
    return sorted(result)

