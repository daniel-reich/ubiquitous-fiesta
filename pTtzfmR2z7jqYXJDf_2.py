
possible_palindrome=lambda s:sum(s.count(c)%2for c in set(s))<2

