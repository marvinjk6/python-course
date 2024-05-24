# For Loop in Python

For Loop:

- A for loop in Python is used to iterate over a sequence of values.

range function:

- Produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
  range(i, j) produces i, i+1, i+2, ..., j-1  
  When step is given, it specifies the increment (or decrement).
- start
- stop
- step

Indentation is crucial:

- If you skip indentation, you'll encounter an IndentationError.
  Nested loop

Nested loop:

- A for loop can be nested inside another for loop, and this is known as a nested loop. The inner loop executes completely for each iteration of the outer loop.

Formatted String Literals (f-strings)

- print(f"The sum is {variable}")

### Section Quiz

1. Given the syntax of a for loop below, what is the role of val? for val in sequence:

- During each iteration of the loop, val takes on the value of the current item in the sequence.

2. What does the range(1,10) function do in the context of a for loop?

- The range() function with arguments 1 and 10 will generate a sequence of numbers starting from 1 up to, but not including, 10.

3. What is a nested for loop in Python?

- What is a nested for loop in Python?

4. Why are nested loops beneficial in programming?

- Nested loops enable the creation of multi-level or multi-dimensional iterations, which can be useful for tasks like traversing matrices, generating combinations, and more.
