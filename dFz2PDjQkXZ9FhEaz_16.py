
def letter_check(lst):
    for i in range (len(lst)):
        if i==1:
            STRING2 = lst[1]
            STRING1 = lst[0]
            for elem in STRING2:
                if elem not in STRING1 and elem not in STRING1.lower():
                    print('NO')
                    return False
    print("YES")
    return True

