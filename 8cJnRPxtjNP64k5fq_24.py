
def dance(lst, parameter):
    women, men = [], []
    for pair in lst:
        woman, man = pair
        women.append(woman)
        men.append(man)
    if parameter == 'women':
        return [[w, m] for w, m in zip(women[::-1], men)]
    return [[w, m] for w, m in zip(women, men[::-1])]

