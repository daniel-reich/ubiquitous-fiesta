
def balanced(lst):
    half = len(lst)//2
    return max(lst[:half], lst[half:]) * 2 if sum(lst[:half]) != sum(lst[half:]) else lst

