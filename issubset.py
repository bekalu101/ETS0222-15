a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # Output: True
print(b.issuperset(a)) # Output: True
print(a.isdisjoint({4, 5}))  # Output: True
