
def get_best_student(grades):
    n_lst = []
    for i in grades:
        n_lst.append(str(int(sum(grades[i])/len(grades[i]))) + str(i))
    return sorted(n_lst)[-1][2::]

