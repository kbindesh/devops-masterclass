# Understand how to handle errors in Python

In this module, we will learn how to handle exceptions in Python using `try`, `except`, and `finally` statements with the help of examples.   

In python, there could be basically two types of errors:
    1) Syntax Errors
    2) Exception Errors

## Advantages of handling Exceptions in the program
   - Clean code
   - Easier debugging
   - Easier to read & maintain the code
   - Better application reliability
   - Better end-user experience

## [Different types of Exceptions](https://docs.python.org/3/library/exceptions.html)
   - In Python, there are various built-in exceptions that can be raised when an error occur while executing a program.
   - Here are some of the most common types of Python exceptions:
     - NameError
     - SyntaxError
     - TypeError
     - IndexError
     - KeyError
     - ValueError
     - IOError

## Syntax Error vs Exceptions - Example

### 1. Syntax Error

### 2. Exception (Runtime errors)

## `try` and `except` statements for catching exceptions
   ```
   n = int(input('Enter numerator'))
   d = int(input('Enter denominator'))

   try:
      result = n/d
      print(result)
   except ZeroDivisionError:
      print('Divide by zero error')

   print('continue to execute rest of the logic...')

   ```

## `try-except-else` statements for catching exceptions
   ```
   n = int(input('Enter numerator'))
   d = int(input('Enter denominator'))
   
   try:
      result = n/d
   
   except ZeroDivisionError:
      # write the code we want to execute when exception occurs
      print('Divide by zero error')
   else:
      print(result)
   ```

## `finally` block
   ```
   n = int(input('Enter numerator'))
   d = int(input('Enter denominator'))
   
   try:
      result = n/d
      print(result)
   except ZeroDivisionError:
      # write the code we want to execute when exception occurs
      print('Divide by zero error')
   finally:
      print('This code will be executed no matter what')
   ```

## Catching specific exceptions