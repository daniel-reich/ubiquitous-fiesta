
def briscola_score(my_deck1, my_deck2):
    my_point1 = 0
    my_point2 = 0
    dic = {"A": 11, "3": 10, "K": 4, "Q": 3, "J": 2}
    for card, value in dic.items():
        num1 = 0
        num2 = 0
        while num1 < len(my_deck1):
            if card in my_deck1[num1]:
                my_point1 += value
            num1+=1
        while num2 < len(my_deck2):
            if card in my_deck2[num2]:
                my_point2 += value
            num2+=1
    if (120-my_point1) < my_point2:
        return "You Win!"
    elif (120-my_point1) > my_point2:
        return "You Lose!"
    else:
        return "Draw!"

