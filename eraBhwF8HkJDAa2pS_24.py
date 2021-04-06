
def pirates_killed(gold, tolerance):
    major = max(gold)
    diff = [major - elem for elem in gold]
    for i in range(len(tolerance)):
        if tolerance[i] < diff[i]:
            return True
    return False

