
def retrieve(text):
    vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
    res_list = []
    lst = []
​
    if text != "":
        lst = text.split(" ")
        for item in lst:
            if item[0] in vowels:
                new_item = item.replace(".", "")
                res_list.append(new_item.lower())
        return res_list
    else:
        return res_list

