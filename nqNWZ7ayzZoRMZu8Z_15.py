
def avg_note(students):
    myans = []
​
    for i in range(len(students)):
        d = {}
        ctr = 0
        for j in range(len(students[i]['notes'])):
            ctr += students[i]['notes'][j]
        if len(students[i]['notes']) == 0:
            ctr = 0
        else:
            ctr = ctr / len(students[i]['notes'])
​
        if students[i]['name'] not in d:
            d['name'] = students[i]['name']
            d['avgNote'] = round(ctr,0)
        myans.append(d)
    return myans

