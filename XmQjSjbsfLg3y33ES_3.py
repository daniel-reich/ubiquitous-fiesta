
def legalbacklog(cases, max_daily_sessions):
    cnt = 0
    cases = sorted(cases.values(), reverse = True)
    while len(cases) > 0:
        cnt += 1
        for i in range(min(len(cases), max_daily_sessions)):
            cases[i] -= 1
        cases = sorted([c for c in cases if c > 0], reverse = True)
    return cnt

