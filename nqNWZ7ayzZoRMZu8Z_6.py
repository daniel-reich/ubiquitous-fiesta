
def avg_note(students):
    ans = []
    for d in students:
        if len(d["notes"]) > 0:
            ans.append({"name": d["name"], "avgNote": int(round(sum(d["notes"]) / float(len(d["notes"])), 0))})
        else:
            ans.append({"name": d["name"], "avgNote": 0})
    return ans

