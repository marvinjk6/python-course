

def are_both_even(i, j):
  is_i_even = i % 2 == 0
  is_j_even = j % 2 == 0

  return is_i_even and is_j_even

print(are_both_even(4, 2))  # Output: True
print(are_both_even(3, 4))  # Output: False