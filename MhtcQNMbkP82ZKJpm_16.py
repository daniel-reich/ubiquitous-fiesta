
def get_notes_distribution(students):
    d = {}
    for dic in students:
        lon = dic['notes']
        for n in lon:
            if n in [1, 2, 3, 4, 5]:
                if n not in d:
                    d[n] = 0
                d[n] += 1
    return d

