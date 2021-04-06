
def rotate_transform(lst, num):
    list_of_tuples = zip(*lst[::-1])
    a=[list(elem) for elem in list_of_tuples]
    if num==-1 or num==3:
        return [ele[::-1]for ele in a][::-1]
    if num==2 or num==-2 :
        return [ele[::-1]for ele in lst[::-1]]
    if num==5or num==1:
        return a
    if num==-5:
        return [ele[::-1]for ele in a[::-1]]
    else:
        return lst

