
def count_smileys(lst):
​
    count = 0
​
    for smileys in lst:
​
        if len(smileys) == 3:
​
            if smileys[0] == ":" or smileys[0] == ";" :
​
                if smileys[1] == "-" or smileys[1] == "~":
​
                    if smileys[2] == ")" or smileys[2] == "D":
​
                        count = count + 1
​
        elif len(smileys) == 2:
​
            if smileys[0] == ":" or smileys[0] == ";":
​
                if smileys[1] == ")" or smileys[1] == "D":
​
                    count = count + 1
​
    return count

