
def first_n_vowels(str1,n):
    new_list = []
    for char in str1:
        if char in "aeiou":
            new_list.append(char)
    if n > len(new_list):
        return "invalid"
    return "".join(new_list[:n])

