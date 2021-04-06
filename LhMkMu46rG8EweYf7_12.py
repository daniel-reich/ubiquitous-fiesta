
import string
​
lowercase = string.ascii_lowercase
def get_key(ele):
    count = 0
    for val in ele:
​
        if val in lowercase:
            return ele[count]
        else: count +=1
​
def sort_by_letter(lst):
    return sorted(lst, key = get_key)

