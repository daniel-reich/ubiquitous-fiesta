
def pizza_points(customers,num,price):
    name_list= []
    for name,items in customers.items():
        count = 0
        for i in items:
            if i >= price:
                count += 1
            if count >= num and name not in name_list:
                name_list.append(name)
    return sorted(name_list)

