
def vowels(string):
    vow_times = 0
    vow_list = ["a", "e", "i", "o", "u"]
    if len(string) < 1:
        return vow_times
    if string[0] in vow_list:
        vow_times += 1
    return vow_times + vowels(string[1:])

