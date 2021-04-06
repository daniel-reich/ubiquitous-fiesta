
def get_student_top_notes(lst):
    l1 = []
    for a in lst:
        if a['notes']:
            l1.append(max(a['notes']))
        else:
            l1.append(0)
    return l1

