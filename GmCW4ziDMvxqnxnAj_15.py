
def who_passed(students):
    not_pass = []
    for key, value in students.items():
        for grade in value:
            breuk = grade.split("/")
            if breuk[0] != breuk[1]:
                not_pass.append(key)
                continue
​
    for person in set(not_pass):
        students.pop(person)
    
    passed = sorted([student for student in students])
    return passed

