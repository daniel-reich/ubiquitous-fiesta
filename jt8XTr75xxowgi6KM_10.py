
def get_student_top_notes(l):
    nl = []
    for d in l:
        nl.append(max(d['notes'])) if d['notes'] else nl.append(0)
    return nl

