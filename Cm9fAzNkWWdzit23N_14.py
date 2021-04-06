
wave = lambda word: [word[:upper_letter_num] + word[upper_letter_num].upper() + word[upper_letter_num + 1:] for upper_letter_num in range(len(word)) if not word[upper_letter_num] == " " ]

