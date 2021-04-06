
def greatest_impact(lst):
    weather = sum([i[1] for i in lst])
    meals = round(sum([i[2]*3.33333333333333 for i in lst]))
    sleep = sum([i[3] for i in lst])
    a = [weather, meals, sleep]
    if weather == meals == sleep:
        return "Nothing"
    elif min(a) == weather:
        return "Weather"
    elif min(a) == meals:
        return "Meals"
    else:
        return "Sleep"
  # lst in format: [Mood, Weather, Meals, Sleep]

