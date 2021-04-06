
def progress_days(n):
      return sum(1 for m in range(1,len(n)) if n[m] > n[m-1])

