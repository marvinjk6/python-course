# Data Types

## Numeric Data Type

In Python, numbers are represented by two fundamental data types: integers and floating-point numbers, referred to as int and float, respectively.

### Integer

- An integer is a whole number, without a fraction.
- Examples include 1, 2, 6, -1, and -2. int

### Floating Point Numbers

- Floating-point numbers, or floats, represent real numbers and are written with a decimal point dividing the integer and fractional parts.
- Examples include 2.5 and 2.55.

### Integer division

- The double slash operator (//) performs integer (or floor) division. 5//2 results in 2.

### Remember:

- Operations can also be performed between int and float. The result of an operation between an int and a float is always a float.
  - 4 / 2 = 2.0
- Use == for comparison and = for assignment.
- floating-point numbers can't always precisely represent real numbers in the binary format used by computers.
  - 4.2 - 3.5 = 1.2999999999999998

### Decimal:

- If you're dealing with highly sensitive financial calculations, don't use floats to represent your values due to their precision issues. Instead, use the Decimal data type.

### Increment and Decrement operators:

- Shorthand to increment a variable. i += 1. Similar operators -=, /=, \*=
- Python does'nt support ++ or -- operators

### Typing conversion

- float()
- int()
- round()

### Dynamic Typing

- In Python, the type of a variable can change during the execution of a program

### Boolean Values

- In Python, True and False are the Boolean values.
- always Capitalized

### Section Quiz

1. Which of the following is the correct class for integers in Python?

- int

2. Which of the following statements is true regarding floating-point numbers in Python?

- In Python 3, dividing using the / operator always returns a floating-point number, even if the division is exact. For instance, 4 / 2 would return 2.0.

3. What is the result of the operation between an int and a float?

- float

4. What is the recommended data type for sensitive financial calculations due to precision issues with floats?

- The Decimal type in Python provides arbitrary precision and is designed for financial calculations where precision is crucial.

5. What happens when you try to use the i++ or ++i syntax in Python?

- Python does not support the post-increment (i++) or pre-increment (++i) syntax. Attempting to use it will result in a syntax error.

6. Which operator performs integer (or floor) division in Python?

- // operator

7. How do you perform exponentiation in Python?

- Using \*\*

8. What function in Python can be used to convert a floating point number to its nearest integer?

- round()

9. Which of the following correctly represents Boolean values in Python?

- True and False
