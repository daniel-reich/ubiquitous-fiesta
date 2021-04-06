
def get_best_student(grades):
    a = max([sum(grades[i]) for i in grades])
    return [i for i in grades if sum(grades[i]) == a][0]

