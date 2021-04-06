
def clean_up_list(lst):
    return [[int(i)for i in lst if int(i)%2==0],[int(i)for i in lst if int(i)%2!=0]]

