# Python program flow control statements

## `if` statement
   ```
   # Syntax

   if (condition):
     <Block of code to execute if condition is found to be true>

   # Example

   if (num > 10):
     print('Num is greater than 10')
   ```

## `if-else` statement
   ```
   # Syntax

   if (condition):
     <Block of code to execute if condition is found to be TRUE>
   else:
     <Block of code to execute if condition is found to be FALSE>
   
   # Example

   if (num >= 10):
     print('Num is greater than or equal to 10')
   else:
     print('Num is less than 10')
   ```

## `if-elif-else` statement
   ```
   # Syntax

   if (condition-01):
     <Block of code to execute if condition-01 is found to be TRUE>
   elif (condition-02):
     <Block of code to execute if condition-02 is found to be TRUE>
   elif (condition-N)
     <Block of code to execute if condition-N is found to be TRUE>
   else:
     <Block of code to execute if none of the above condition is found to be TRUE>

   # Example

   if (num >= 10):
     print('Num is greater than or equal to 10')
   elif (num <= 10):
     print('Num is less than or equal to 10')
   else:
     print('All the previous conditions are FALSE')
   ```

## `Nested if` Statements
   