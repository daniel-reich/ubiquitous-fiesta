
def schoty(lines):
  reversed_lines  = lines[::-1];
  return sum([read_line(reversed_lines[idx]) * (10**idx) for idx in range(0, len(lines))]);
  
def read_line(line):
  return len(line.split("---")[0]);

