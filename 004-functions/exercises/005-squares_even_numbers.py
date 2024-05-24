
# soma do quadrado de n números pares

def sum_of_squares(n):
  sum_squares = 0
  for i in range(2, n * 2 + 1, 2):
    # print(i)
    sum_squares = sum_squares + (i*i)
  return sum_squares

print(sum_of_squares(5))
