
is_palindrome_possible = lambda txt : sum(1 if txt.count(ch) == 1 else 0 for ch in txt) in [0,1]

