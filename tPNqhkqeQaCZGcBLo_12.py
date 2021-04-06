
def determine_who_cursed_the_most(d):
    me, spouse = 0, 0
​
    for v in d.values():
        me += v['me']
        spouse += v['spouse']
​
    answer = {'ME!': me > spouse, 'SPOUSE!': spouse > me, 'DRAW!': me == spouse}
    for r in answer:
        if answer[r]:
            return r

