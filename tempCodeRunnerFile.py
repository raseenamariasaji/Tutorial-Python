import functools

s = ["Programming in Python", "Hello", "Be happy"]
vowel_count = functools.reduce(lambda count, item: count + sum(1 for char in item if char in "aeiouAEIOU"), s, 0)
print(vowel_count)
