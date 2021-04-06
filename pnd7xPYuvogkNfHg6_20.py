
def get_best_student(grades):
    students = {}
    for i in grades:
        key = i
        value = grades[key]
        average = sum(value)/len(value)
        students[int(average)]=key
    highest_number = sorted([i for i in students], reverse=True)
    answer = students[highest_number[0]]
    return answer

