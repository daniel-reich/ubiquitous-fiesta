
def round_number(num, n):
  down, up = num%n, -num%n
  return num - down if down < up else num + up

