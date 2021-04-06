
ascii_sort = lambda lst: sorted(lst, key=lambda word: sum([ord(letter) for letter in word]))[0]

