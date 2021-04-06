
def max_separator(str):
    max_width = 0
    best_letter = dict()
    for position in range(len(str)):
        
        length = 0
        current = str[position]
        
        for letter in str[position + 1:]:
            length += 1
            if letter == current:
                if (length >= max_width):
                    
                    best_letter[current] = length;
                    
                    max_width = length
                    break
                else:
                    break
​
            
    longest_substring_letters = []
    for i in best_letter:
        if best_letter[i] == max_width:
            longest_substring_letters.append(i)
        
    return sorted(longest_substring_letters)

