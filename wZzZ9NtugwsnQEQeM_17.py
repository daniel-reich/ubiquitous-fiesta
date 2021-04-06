
scoring = {'eagle':-2,'birdie':-1
,'par':0,
'bogey':1,
'double-bogey':2,}
​
def golf_score(course, result):
    score = 0
    for cours,reslt in zip(course,result):
        if reslt in scoring.keys():
            score += cours + scoring[reslt]
    return score

