
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:40:52 2020
​
@author: fabin
"""
​
​
def prime(n):
  if n == 1:
    return False
  for i in range(2,((n//2)+1)):
    if n%i == 0:
      return False
  return True
    
def truncatable(n):
  if not prime(n):
    return False
  left = True
  right = True
  n_str = str(n)
  while len(n_str)>1 and left:
    n_list = []
    for i in range(1,len(n_str)):
      n_list.append(n_str[i])
    str2 = n_list[0]
    if '0' in n_list:
      left = False
      right = False
    for i in range(1,len(n_list)):
      str2 = str2 + n_list[i]
    n_left = int(str2)
    if not prime(n_left):
      left = False
    n_str = str(n_left)
  n_str = str(n)
  while len(n_str)>1 and right:
    n_list = []
    for i in range(0,(len(n_str)-1)):
      n_list.append(n_str[i])
    str2 = n_list[0]
    for i in range(1,len(n_list)):
      str2 = str2 + n_list[i]
    n_right = int(str2)
    if not prime(n_right):
      right = False
    n_str = str(n_right)
  if left and not right:
    return "left"
  elif right and not left:
    return "right"
  elif left and right:
    return "both"
  else:
    return False

