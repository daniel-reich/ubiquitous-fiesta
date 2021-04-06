
def bitwise_index( lst ) :
    largest_integer = -9999999999999999
    index_of_largest = "0"
    for i in range(len(lst)) :
        if lst[i] > largest_integer :
            if (int(lst[i] / 2)) * 2 == lst[i] :
                largest_integer = lst[i]
                index_of_largest = str(i)
​
​
    if largest_integer > -9999999999999999:
        if index_of_largest=="0":
            return {"@even index " + index_of_largest : largest_integer}
​
        elif index_of_largest=="1":
            return {"@odd index " + index_of_largest : largest_integer}
​
        elif (int(int(index_of_largest) / 2) * 2) == int(index_of_largest):
            return {"@even index " + index_of_largest : largest_integer}
​
        elif (int(int(index_of_largest)  / 2) * 2) != int(index_of_largest):
            return {"@odd index " + index_of_largest : largest_integer}
    else :
        return "No even integer found!"

