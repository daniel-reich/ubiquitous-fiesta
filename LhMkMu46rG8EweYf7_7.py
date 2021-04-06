
def sort_by_letter(lst):
  def helper(word):
    for letter in word:
      if letter.isalpha():
        return letter
  
  return sorted(lst, key=helper) if lst else []

