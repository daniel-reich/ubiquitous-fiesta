
def who_goes_free(n, k):
  if n == 1:
    return 0
  return (who_goes_free(n - 1, k) + k) % n

