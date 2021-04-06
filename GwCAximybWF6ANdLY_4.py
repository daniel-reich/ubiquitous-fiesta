
def pie_chart(data):
  total_frequencies = 0
  data_copy = data
​
  for label in data:
    total_frequencies += data[label]
​
  for label in data_copy:
    data_copy[label] = round((data_copy[label] / total_frequencies) * 360, 1)
​
  return data_copy

