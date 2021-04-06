
replace_the=lambda t:' '.join(['an'if x=='the'and y[0]in'aeiou'else 'a'if x=='the'else x for x,y in zip(t.split(),t.split()[1:]+[' '])])

