
from numpy import corrcoef
def greatest_impact(lst):
    factor_names = ['Weather', 'Meals', 'Sleep']
    mood, weather, meals, sleep = [], [], [], []
    for sub_lst in lst:
        mood.append(sub_lst[0])
        weather.append(sub_lst[1])
        meals.append(sub_lst[2])
        sleep.append(sub_lst[3])
    if len(set(mood)) == 1:
        return 'Nothing'
    correlations = [corrcoef(mood, weather)[0][1], corrcoef(mood, meals)[0][1],
                    corrcoef(mood, sleep)[0][1]]
    max_abs_corr = max(correlations, key=abs)
    return factor_names[correlations.index(max_abs_corr)]

