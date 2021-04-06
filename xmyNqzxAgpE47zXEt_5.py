
def is_alphabetically_sorted(sentence):
    sentence = sentence.replace(".","")
    sentence = sentence.lower()
    my_str = "paula"
    my_list = []
    sorted_list = []
    string = ""
    lst = []
    for i in range (0,len(sentence)):
        lst = sentence.split()
        for j in range (0,len(lst)):
            string = lst[j]
            my_list = []
            sorted_list = []
            for k in range (0,len(string)):
                my_list.append(string[k])
            for l in range (0,len(my_list)):
                sorted_list.append(my_list[l])
            sorted_list.sort()
            #print(my_list)
            #print(sorted_list)
            if (sorted_list == my_list and len(my_list) > 2):
                return True
    return False
        
​
print(is_alphabetically_sorted("Paula has a French accent."))

