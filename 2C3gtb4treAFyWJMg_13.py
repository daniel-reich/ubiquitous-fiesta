
chars = [chr(i) for i in range (97,123) if i != 106]
nums = [str(i) + str(j) for i in range (1,6) for j in range (1,6)]
​
def polybius(txt):
  if txt[0].isalpha():
    txt = txt.lower().replace("j","i")
    return " ".join("".join(nums[chars.index(c)] for c in w if c.isalpha()) for w in txt.split())
  return " ".join("".join(chars[nums.index(w[i:i+2])] for i in range (0,len(w),2)) for w in txt.split())

