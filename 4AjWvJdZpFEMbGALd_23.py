
def who_goes_free(n, k):
    members = list(range(n))
    count = 1
    while len(members) > 1:
        for x in range(len(members)):
            if count == k:
                members[x] = '-'
                count = 1
            else:
                count += 1
        members = [member for member in members if member != '-']
    return members[0]

