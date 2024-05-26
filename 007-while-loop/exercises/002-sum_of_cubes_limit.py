
def sum_of_cubes_up_to_limit(limit):
  i = 1
  sum = 0
  while i * i * i <= limit:
    sum += i * i * i
    i += 1
  return sum

# Sum = 1 + 4 + 9 + 16 + 25 = 55
print(sum_of_cubes_up_to_limit(30)) 