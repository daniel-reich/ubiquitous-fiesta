
def arrow(num):
  when_odd = [">" * i for i in range(1, num)]
  when_even = [">" * i for i in range(1, num + 1)]
  return (when_odd + [">" * num] + when_odd[::-1]) if (num % 2 != 0) else (when_even + when_even[::-1])

