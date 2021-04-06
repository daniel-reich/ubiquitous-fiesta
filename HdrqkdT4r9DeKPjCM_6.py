
def is_polygonal(n):
    if n == 1:
        return "0th of all"
    if n<=3:
        return False
    result_list =[]
    side = n-1
    
    def result(x, side):
        if x == 1:
            return '1st ' + str(side) + '-gonal number'
        elif x == 2:
            return '2nd ' + str(side) + '-gonal number'
        elif x == 3:
            return '3rd ' + str(side) + '-gonal number'
        elif int(list(str(x))[-1])== 1 and x>11:
            return str(x)+'st ' + str(side) + '-gonal number'
        else:
            return str(x)+'th ' + str(side) + '-gonal number'
    
    for i in range(2,side):
        test = i+1
        if side%test == 0:
            count = 2
            y = test
            while y < side:
                y +=test*count
                count += 1
            count -= 1
            if y == side:
                result_list.append(result(count,test))
            else:
                continue
    return result_list

