
vowels=lambda n:0if n==''else vowels(n[:-1])+1if n[-1]in'aeiou'else vowels(n[:-1])

