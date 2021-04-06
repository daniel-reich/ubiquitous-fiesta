
def get_student_top_notes(students):
    ll = []
    for i in students:
        if i["notes"] != []:
            ll.append(max(i["notes"]))
        elif i["notes"]==[]:
            ll.append(0)
    return ll

