
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
def change(x, times):
    new_list = x.copy()
    for i in range(len(new_list)):
        j = 1
        while j <= times:
          if i >= j and i < len(new_list)-j:
            new_list[i] -= 1
          j += 1
    return new_list
​
x = [3, 3, 3, 3, 3, 3, 3]

