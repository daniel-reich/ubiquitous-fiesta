
def get_products(lst):
    array1 = []
    for index in range(len(lst)):
        counter = 0
        temp = 1
        for i in lst:
            if index != counter:
                temp = temp*i
            counter = counter + 1
        array1.append(temp)
    return array1

