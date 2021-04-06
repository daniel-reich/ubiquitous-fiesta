
def get_best_student(grades):
    for student in grades.keys():
        grades[student] = sum(grades[student])//len(grades[student])
    return {y:x for x,y in grades.items()}[max({y:x for x,y in grades.items()}.keys())]

