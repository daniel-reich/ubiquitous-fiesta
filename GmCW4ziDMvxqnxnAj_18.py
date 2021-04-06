
def who_passed(students):
    newlist = []
    for eachstudent in students.keys():
        if sum(list([int(eval(x)) for x in students[eachstudent]])) == len(students[eachstudent]):
            newlist.append(eachstudent)
    return sorted(newlist)

