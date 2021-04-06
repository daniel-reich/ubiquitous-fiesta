
def group_seats(lst, n):
    return sum([1 for row in lst for i in range(len(row)-1) if row[i:i+n] == [0 for i in range(n)]])

