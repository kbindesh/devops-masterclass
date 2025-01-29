# Introduction to Python Functions
  - A function is a block of code which performs a particular task and only runs when it is called.
  - The idea is to put some repeatedly done tasks together and out them into a  function so that instead of writing the same code again and again for different inputs, we can simply call the functions to reuse code contained in it over and over again.

## Function Declaration
   - The syntax to declare a function:

   ```
   def <function_name> (param1,param2,...,param-n):
       
       # your function logic here
       
       return <expression>
   ```

## Types of Function in Python
   - There are mainly two types of functions, namely:
     1) **Built-in Functions** - These are standard functions whose logic is already known to the Python interpreter and are readily available for use.
        
     2) **Custom Functions** - These functions are with custom logic that we need write based on the business reqiurements

## Create a Python Function
   ```
   def hello_msg():
       print("Hello world..")

   ```
## Calling a Python Function
   ```
   # Function defination
   def hello_msg():
       print("Hello world")
   
   # Calling a function
   hello_msg()

   ```
## What are `Arguments` and `Parameters` in Python?

### Python Arguments
   - If you want to send some information to your function while calling, that can be passed into functions as an *Argument*.
   - Arguments are specified after the function name, inside the parentheses.
   - It can be a variable, value or an object passed to a function or method as input.
   - You can add as many arguments as you want, just separate them with a comma.
   - **Example**
     
     ```
     # Function defination
     def print_msgs(fname):
        print("Hello world")
    
     # Calling a function 1st time with an argument
     print_msgs("Krishna")

     # Calling a function 2nd time with different argument
     print_msgs("Guido Van")
     
     # Calling a function 3rd time with different argument
     print_msgs("Vedika")      
     ```
### Python Parameters
   - A *Parameter* is the variable defined within the parentheses during function definition. 
   - We define *Parameters* when we declare/define a function. 
   - **Example**
     
     ```
     # Function defination with a Parameter 'fname' to map it with the passed argument
     def calc_sum(fname):
        print("Hello world")
    
    
     # Calling a function 1st time with an argument
     print_msgs("Krishna")

     # Calling a function 2nd time with different argument
     print_msgs("Guido Van")
     
     # Calling a function 3rd time with different argument
     print_msgs("Vedika")      
     ```
## Return the values from a Function

