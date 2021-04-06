
def can_enter_cave(x):
    def common_data(list1, list2): 
        result = False 
        for x in list1: 
            for y in list2:
                if x == y: 
                    result = True
        return result
    def transpose(m): #Swaps rows and columns. Columns are MUCH easier for this.
        return[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    x = transpose(x)
    zeros = []
    for k in x: 
        zeros.append([i for i, j in enumerate(k) if j == 0])
    for z in range(1,len(zeros)):
            if False in [common_data(zeros[z-1],zeros[z])]:
                return False
    return True

