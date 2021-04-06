
def playfair(text, keyword):
    length = len(keyword)
    map_table = []
    for i in range(length):
        if (keyword[i] >='a' and keyword <='z') or (keyword[i] >='A' and keyword <='Z'):
            upper = keyword[i].upper()
            if upper == 'J':
                upper == 'I'
            if upper not in map_table:
                map_table.append(upper)
    for i in range(ord('A'), ord('Z')+1):
        upper = chr(i)
        if upper == 'J':
            upper = 'I'
        if upper not in map_table:
            map_table.append(upper)
    
    plain = []
    length = len(text)
    plain_flag = 1
    count = 0
    for i in range(length):
        if (text[i] >='a' and text[i] <='z') or (text[i] >='A' and text[i] <='Z'):
            plain.append(text[i].lower())
        else:
            plain_flag = 1
        if text[i] >='A' and text[i] <='Z':
            count = count + 1
    
    if count == length:
        plain_flag = 0
        
    
    #split to 2 character block
​
    i = 0
    while(i<len(plain)):
        if (i+1) < len(plain):
            if plain[i] == plain[i+1]:
                 plain.insert(i+1, 'x')
        i = i + 2
    if len(plain)%2 == 1:
        plain.append('x')
                
                
    #encode
    result = []
    length = len(plain)
    for i in range(0, length, 2):
        upper = plain[i].upper()
        if upper == 'J':
            upper = 'I'
        first_index = map_table.index(upper)
        upper = plain[i+1].upper()
        if upper == 'J':
            upper = 'I'
        second_index = map_table.index(upper)
        
        first_row = int(first_index/5)
        first_col = first_index%5
        
        second_row = int(second_index/5)
        second_col = second_index%5
        
        if first_row == second_row:
            if plain_flag == 1:
                first_index_new = first_row*5 + (first_col+1)%5
                second_index_new = second_row*5 + (second_col+1)%5
            else:
                first_index_new = first_row*5 + (first_col+4)%5
                second_index_new = second_row*5 + (second_col+4)%5
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
        elif first_col == second_col:
            if plain_flag == 1:
                first_index_new = ((first_row+1)%5)*5 + first_col
                second_index_new = ((second_row+1)%5)*5 + second_col
            else:
                first_index_new = ((first_row+4)%5)*5 + first_col
                second_index_new = ((second_row+4)%5)*5 + second_col
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
        else:
            first_index_new = first_row*5 + second_col
            second_index_new = second_row*5 + first_col
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
            
    result_str = ""
    for item in result:
        result_str = result_str + item
    return result_str

