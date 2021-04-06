
def get_best_student(grades):
    m = 0
    n = ''
    for i,j  in grades.items():
        z = sum(j) / len(j)
        if z > m:
            m = z
            n = i
    else:
        return n

