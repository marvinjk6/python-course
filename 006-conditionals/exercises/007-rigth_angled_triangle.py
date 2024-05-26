
def is_right_angled_triangle(side1, side2, side3):
  if(side1 <= 0 or side2 <=0 or side3 <= 0):
    return False
  
  side1_square = pow(side1, 2)
  side2_square = pow(side2, 2)
  side3_square = pow(side3, 2)

  if(side1_square == side2_square + side3_square):
    return True
  
  if(side2_square == side1_square + side3_square):
    return True
  
  if(side3_square == side1_square + side2_square):
    return True
  
  return False

print(is_right_angled_triangle(5, 5, 5))
print(is_right_angled_triangle(3, 4, 5))  # Output: True
