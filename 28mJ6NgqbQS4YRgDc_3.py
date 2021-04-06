
def can_pay_cost(mana_pool, cost):
    colours = ["R", "W", "B", "U", "G", "C"]
    manacolours = []
    costcolours = []
    playable = True
    anycolour = ""
    for i in range(0,6):
        manacolours.append(mana_pool.count(colours[i]))
        costcolours.append(cost.count(colours[i]))
    for i in cost:
        if i.isnumeric() == True:
            anycolour += i
    if anycolour == "":
        anycolour = 0
    anycolour = int(anycolour)
    for i in range(0,6):
        if manacolours[i] < costcolours[i]:
            playable = False
    if anycolour + sum(costcolours) > len(mana_pool):
        playable = False
    return playable

