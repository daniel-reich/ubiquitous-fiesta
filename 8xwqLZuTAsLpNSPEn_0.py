
def award_prizes(names):
    awards = ['Gold', 'Silver', 'Bronze'] + ['Participation']*(len(names)-3)
    ranked = sorted(names, key=names.get, reverse=True)
    return dict(zip(ranked, awards))

