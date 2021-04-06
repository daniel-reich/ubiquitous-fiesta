
neighbours = {'0': '08', '1': '124', '2': '1235', '3': '236', '4': '1457',
              '5': '24568', '6': '3569', '7': '478', '8': '57890', '9': '689'}
​
def crack_pincode(pincode):
    possible = [""]
    for digit in pincode:
        new_possible = []
        for poss in possible:
            for neighbour in neighbours[digit]:
                new_possible.append(poss + neighbour)
        possible = new_possible
    possible.sort()
    return possible

