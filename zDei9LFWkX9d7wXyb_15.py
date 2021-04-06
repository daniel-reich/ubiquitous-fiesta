
def malthusian(food_growth, pop_mult):
    year = 0
    food, pop = 100, 100
    while food>=pop:
        food+=food_growth
        pop*=pop_mult
        year+=1
​
    return year

