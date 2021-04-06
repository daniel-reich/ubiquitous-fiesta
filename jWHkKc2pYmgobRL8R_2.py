
distance_to_nearest_vowel=lambda t:[min(abs(i-j)for i,y in enumerate(t)if y in'aeiou')for j in range(len(t))]

