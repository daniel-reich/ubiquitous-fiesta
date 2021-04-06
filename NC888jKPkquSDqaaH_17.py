
import numpy as np
def clean_up(files, sort):
  # https://edabit.com/challenge/NC888jKPkquSDqaaH
  key = 0
  if sort == "suffix": 
    key = 1
​
  sorting_list = []
  # Create prefix or suffix list to sort by
  for project in files:
    sorting_info = project.split(".")[key]
    if sorting_info not in sorting_list:
      sorting_list.append(sorting_info)
​
  cleaned_list = [[] for i in range(len(sorting_list))]
  #print(sorting_list)
​
  # Sort into the list
  for n, keyword in enumerate(sorting_list):
    for project in files:
      sorting_info = project.split(".")[key]
      if keyword == sorting_info:
        cleaned_list[n].append(project)
  return cleaned_list

