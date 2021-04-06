
def valid_name(name):
    name_list = name.split()
​
    if len(name_list) != 2 and len(name_list) != 3:
        return False
​
    if len(name_list[0]) == 1:
        return False
    if len(name_list[1]) == 1:
        return False
    if name_list[0] != name_list[0].title():
        return False
    if name_list[1] != name_list[1].title():
        return False
​
    if len(name_list) == 3:
​
​
        if len(name_list[2]) == 1 or "." in name_list[2]:
                return False
        if name_list[2] != name_list[2].title():
                return False
​
        if len(name_list[0]) == 2 and "." in name_list[0]:
            first_name = "initial"
            if (name_list[0][1]) != ".":
                return False
        else:
            first_name = "word"
            if "." in name_list[0]:
                return False
​
        if len(name_list[1]) == 2 and "." in name_list[1]:
            middle_name = "initial"
            if (name_list[1][1]) != ".":
                return False
        elif first_name == "initial":
            return False
​
        return True
​
    if len(name_list) == 2:
​
        if len(name_list[1]) == 1 or "." in name_list[1]:
                return False
​
        if len(name_list[0]) == 2 and "." in name_list[0]:
            if (name_list[0][1]) != ".":
                return False
        else:
            if "." in name_list[0]:
                return False
​
        return True

