# Exploring Python looping statements

## `while` loop statement
   ```
   # Syntax

   while (condition):
     <code_block>
     <increment_or_decrement_the_counter>

   # Example
   
   counter = 1
   while (counter < 5):
     print('Some logic here')
     counter = counter + 1
   ```

## `for` loop statement
   ```
   # Syntax

   for <index> in <list_of_items>:
     <code_block>
     <in_next_iteration_for_loop_will_consider_next_list_Item>

   # Example:
   
   msg = 'HelloWorld'

   for char in msg:
     print(char) 
   ```

## `break` and `continue` statements

## `range()` function with looping statements
   - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
   - A range() with 2 inputs starts at the first input, and goes up in increments of 1 until 1 less than the second input is reached.
   - When range() is used with 3 inputs, it starts at the first input and goes up by increments equal to the 3rd input until 1 less than the second input is reached.
   - Syntax: range(start, stop, step)
   
   ```
   # Syntax
   define the range with one|two|three arguments

   for <index> in <range>:
     <code_block>
   
   # Example with two range argument
   two_ip_range = range(5,10)  # Range starts from 5 and ends at 10

   for index in two_ip_range:
     print(index) 

   ```


