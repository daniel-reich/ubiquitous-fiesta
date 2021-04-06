
def sorting(s):
​
    import string
    alphabet = string.ascii_lowercase
​
    nums=[char for char in s if (char.lower() not in alphabet)]
    nums.sort()
​
    letters = [char for char in s if (char.lower() in alphabet)]
    letter_set=set([char.lower() for char in s if (char.lower() in alphabet)])
    letters_lst=[]
    
    for letter in letter_set:
        letter_lst=[char for char in letters if char.lower()==letter]
        letter_lst.sort(reverse=True)
        letters_lst.append(''.join(letter_lst))
​
    letters_lst.sort(key=lambda x:x[0].lower())
    return ''.join(letters_lst)+''.join(nums)

