import copy

# Original list with nested lists
original = [1, 2, [3, 4]]

# Create a shallow copy
shallow_copy = copy.deepcopy(original)

# Modify the nested list inside the copy
shallow_copy[2][0] = 99

# Both the original and shallow copy are affected
print("Original:", original, id(original[2]))  # Output: [1, 2, [99, 4]]
print("Shallow Copy:", shallow_copy, id(shallow_copy[2]))  # Output: [1, 2, [99, 4]]
