
def determine_who_cursed_the_most(d):
    me = sum([d['round' + str(_ + 1)]['me'] for _ in range(len(d))])
    sp = sum([d['round' + str(_ + 1)]['spouse'] for _ in range(len(d))])
    if me > sp:
        return 'ME!'
    elif sp > me:
        return 'SPOUSE!'
    else:
        return 'DRAW!'

