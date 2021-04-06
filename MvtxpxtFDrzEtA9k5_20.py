
def palindrome_descendant(num):
  return False if len(str(num)) < 2 else str(num) == str(num)[::-1] or palindrome_descendant(int(''.join(list(map(str, list(map(sum, zip(map(int, str(num)[::2]), map(int, str(num)[1::2])))))))))

