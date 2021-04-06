
def get_student_top_notes(students):
    lst  = []
    for i in range(len(students)):
        if students[i]["notes"] == []:
            lst.append(0)
        else:
            lst.append(max(students[i]["notes"]))
    return lst

