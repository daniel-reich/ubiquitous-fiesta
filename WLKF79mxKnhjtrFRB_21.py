
def is_good_match(lst):
    test=[]
    if len(lst)%2!=0:
        return "bad match"
    else:
        for z in range(0,int((len(lst))/2)):
            test.append(lst[2*z]+lst[2*z+1])
        return test

