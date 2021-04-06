
def most_frequent_char(lst):
    joined_list = ''.join(lst)
    most_frequent = max(joined_list, key=joined_list.count)
​
    output = set(most_frequent)
​
    for character in joined_list:
        if joined_list.count(character) == joined_list.count(most_frequent):
            output.add(character)
    return sorted(list(output))

