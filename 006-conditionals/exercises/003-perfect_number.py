
def is_perfect_number(number):
  if number <= 0:
    return False
  
  divisor_sum = 0

  for i in range(1, number):
    if(number % i == 0):
      divisor_sum += i
  
  return divisor_sum == number    

print(is_perfect_number(6))  # Output: True
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(5))  # Output: False