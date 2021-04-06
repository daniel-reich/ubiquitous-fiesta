
def can_patch(bridge, planks):
    string = ''.join([str(i) for i in bridge])
    result = sorted(list(filter(lambda x: x!=0, [len(i)-1 for i in string.replace('1', ' ').split()])), reverse= True)
    if len(result) > len(planks):
        return False
    else:
        for i in result:
            if i in planks:
                pass
            else:
                return False
        return True

