
def lost_dog(*args):
    new_dict = {}; counter = 1
    for room, house in enumerate(args):
        if 0 in house:
            new_dict["Dog" + str(counter)] = "House ({0}) and Room ({1})".format(room + 1, house.index(0) + 1)
            counter += 1
    return new_dict if len(new_dict) != 0 else "Dog not found!"

