
def build_staircase(height, block):
  return [[block if i <= idx_row else '_' for i in range(height)] for idx_row in range(height)]
  
print(build_staircase(3, '#'))

