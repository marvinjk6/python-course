
def sum_of_squares_up_to_limit(limit):
  i = 1
  sum = 0
  while i * i <= limit:
    sum += i * i
    i += 1
  return sum

print(sum_of_squares_up_to_limit(30)) # Sum = 1 + 4 + 9 + 16 + 25 = 55