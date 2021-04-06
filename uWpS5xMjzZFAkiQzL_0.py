
def odds_vs_evens(n):
    total = sum(int(i) if int(i)%2 else -int(i) for i in str(n))
    return 'odd' if total > 0 else 'even' if total < 0 else 'equal'

