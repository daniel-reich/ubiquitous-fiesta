
def get_only_evens(nums):
      list = []
      for idx, value in enumerate(nums):
        if ((idx%2)==0) & ((value%2)==0):
          list.append(value)
      return list

