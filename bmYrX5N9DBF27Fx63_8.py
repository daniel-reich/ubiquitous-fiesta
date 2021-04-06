
answers = ['Weather', 'Meals', 'Sleep']
​
def greatest_impact(lst):
    # lst in format [Mood, Weather, Meals, Sleep]
    diffs = [0, 0, 0]
    moods = 0
    for mood, weather, meal, sleep in lst:
        moods += mood
        diffs[0] += abs(mood - weather)
        diffs[1] += abs(mood - meal)
        diffs[2] += abs(mood - sleep)
    if moods == 10 * len(lst):
        return 'Nothing'
    m = min(diffs)
    for i in range(3):
        if diffs[i] == m:
            return answers[i]

