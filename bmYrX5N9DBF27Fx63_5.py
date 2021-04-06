
def greatest_impact(lst):
  # lst in format: [Mood, Weather, Meals, Sleep]
    impact = {"Weather":0, "Meals":0, "Sleep":0}
    for i in range(1, len(lst)):
        if lst[i][0] > lst[i-1][0]: #increasing mood
            weather = (lst[i-1][1] - lst[i][1])/10
            meals =  (lst[i-1][2] - lst[i][2])/3
            sleep = (lst[i-1][3] - lst[i][3])/10
        elif lst[i][0] < lst[i-1][0]: #Decreasing mood
            weather = (lst[i][1] - lst[i-1][1])/10
            meals =  (lst[i][2] - lst[i-1][2])/3
            sleep = (lst[i][3] - lst[i-1][3])/10
        else:
            continue
        impact["Weather"] += abs(weather)
        impact["Meals"] += abs(meals)
        impact["Sleep"] += abs(sleep)
​
    return 'Nothing' if not all(impact.values()) else max(impact, key = impact.get)

