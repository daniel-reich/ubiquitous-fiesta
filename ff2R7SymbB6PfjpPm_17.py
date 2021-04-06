
def get_budgets(mylist2):
    total = 0
    for dictionary in mylist2:
        total += dictionary['budget']
    return total

