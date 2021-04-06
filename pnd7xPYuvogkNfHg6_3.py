
def get_best_student(grades):
    return sorted(grades, key= lambda x: sum(grades[x])/len(grades[x]), reverse=True)[0]

