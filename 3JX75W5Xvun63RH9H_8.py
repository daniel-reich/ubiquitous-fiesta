
def describe_num(n):
    d_num = {1:"brilliant" , 2:"exciting", 3:"fantastic", 4:"virtuous", 5:"heart-warming" , 6:"tear-jerking", 7:"beautiful", 8:"exhilarating", 9:"emotional", 10:"inspiring"}
    factor= [no for no in range(1,n+1) if n%no==0 and no<=10]
    return "The most {}" .format(" ".join([d_num[no] for no in factor])) +" number is {}" .format(n) +"!"
    
def lowest_num(num):
    result = all([num %n==0 for n in range(1,11)])
    no = 1
    while result == False:
        result = all([no %n==0 for n in range(1,11)])
        if result == False:
            no += 1
            continue
        else:
            return no
            
#the lowest that use all possible words in the sentence is..
#lowest_num(10) = 2520

