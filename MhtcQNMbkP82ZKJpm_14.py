
def get_notes_distribution(students):
    dic = {i:0 for i in range(1,6)}
    order = []
    for student in students:
        for v in student["notes"]:
            if v in dic:
                dic[v] += 1
                if v not in order:
                    order.append(v)
    return {i:dic[i] for i in order}

