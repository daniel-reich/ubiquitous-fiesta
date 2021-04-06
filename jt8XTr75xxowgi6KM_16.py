
def get_student_top_notes(l):
 return [max(s['notes'])if len(s['notes'])>0else 0 for s in l]

