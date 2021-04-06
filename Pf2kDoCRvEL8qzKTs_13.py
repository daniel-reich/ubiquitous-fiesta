
def order_people(lst, people):
    row_order = []
    total_order = []
    if people > lst[0]*lst[1]:
        return ("overcrowded")
    for n in range(1, lst[0]*lst[1] + 1):
        if n > people:
            row_order.append(0)
        else:
            row_order.append(n)
        if len(row_order) == lst[1]:
            total_order.append(row_order)
            row_order = []
    for i in range(1, len(total_order)):
        if i%2 != 0:
            total_order[i] = total_order[i][::-1]
    return total_order

