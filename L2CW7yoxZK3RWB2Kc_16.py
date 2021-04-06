
def message_to_matrix(message, key_lenght):
    matrix = []
    i = 0
    while i < len(message):
        matrix_row = []
        for _ in range(key_lenght):
            try:
                matrix_row.append(message[i])
            except:
                matrix_row.append(' ')
            i += 1
        matrix.append(matrix_row)
    return matrix
​
​
​
​
def nico_cipher(message, key):
    key_list = list(key)
    key_sort_list = sorted(key_list)
    key_num_list = []
    key_count_dict = dict()
    for letter in key_list:
        for i in range(len(key_sort_list)):
​
            if letter == key_sort_list[i]:
                if letter not in key_count_dict:
                    key_count_dict[letter] = 0
                else:
                    key_count_dict[letter] += 1
                key_num_list.append(i + key_count_dict[letter])
                break
    matrix = message_to_matrix(message, len(key))
    message_new = ''
    for row in range(len(matrix)):
        for i in range(len(key_num_list)):
            for j in range(len(key_num_list)):
                if i == key_num_list[j]:
                    message_new += matrix[row][j]
    return message_new

