
def million_in_month(first_month, multiplier):
    goal = 1000000
    amount_of_money = 0
    amount_of_months = 0
    amount_of_money += first_month
    amount_of_months += 2
    new_new_first_month = first_month
​
    while amount_of_money <= goal:
​
        new_new_first_month = new_new_first_month * multiplier
        amount_of_money += new_new_first_month * multiplier
        amount_of_months += 1
​
    return amount_of_months
​
​
​
print(million_in_month(50, 100))

