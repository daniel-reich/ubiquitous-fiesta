
def party_people(lst):
    people = len(lst)
    temp = [i for i in lst if i <= people]
    if temp == lst:
        return people
    return party_people(temp)

