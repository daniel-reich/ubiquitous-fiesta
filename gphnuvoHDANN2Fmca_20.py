
def odd_sort(list):
    even_positions = []
    odd_numbers = []
    final_list = []
    for a in list:
        if a % 2 == 0:
            even_positions.append(list.index(a))
        if a % 2 != 0:
            odd_numbers.append(a)
            odd_numbers.sort()
    for b in odd_numbers:
        final_list.append(b)
    for c in even_positions:
        final_list.insert(c, list[c])
        
    return final_list

