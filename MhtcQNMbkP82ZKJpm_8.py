
def get_notes_distribution(students):
  nums = [x for s in students for x in s['notes'] if str(x) in '12345']
  return {i: nums.count(i) for i in sorted(set(nums))}

