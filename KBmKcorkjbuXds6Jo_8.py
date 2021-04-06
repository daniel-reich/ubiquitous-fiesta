
def chocolates_parcel(small, big, weight):
    return  min([i for i in range(0,small + 1) 
    if (weight - 2*i)%5 == 0 and (weight - 2*i)//5 <= big ]
    , default = -1)

