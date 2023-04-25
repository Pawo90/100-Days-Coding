# # List comprehension
list = [1,2,3]
print(f"Oryginal list {list}")

# First and classic sollution
new_list = []
for n in list:
    new_list.append(n+1)
print(f"Result with classic solution {new_list}")

# Solution with list comprehension
# new lsit = [new_item for n_element in list with n_elements]
new_list = [n+1 for n in list]
print(f"Result with list comprehension {new_list}")

# Challenge
# doubled = [n+n for n in range(1, 5)]
# print(doubled)

# Conditional list comprehension
# new_list = [new_item for n in items if condition]