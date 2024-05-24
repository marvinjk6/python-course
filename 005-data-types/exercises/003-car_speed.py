
def is_eligible_for_race(max_speed):
  return 200 == max_speed

print(is_eligible_for_race(150))  # Output: False
print(is_eligible_for_race(200))  # Output: True
print(is_eligible_for_race(220))  # Output: False