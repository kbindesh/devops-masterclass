# Understanding Python Modules

## Python Module Types
   1) Built-in Modules (e.g. math, base64, csv, datetime, os, etc.)
   2) User defined Modules
   
## Importing Modules
   
   ```
   # Syntax
   import <module_name>

   # Examples
   import math

   import os

   import dir

   ```

## `math` Python module

   ```
   # Import Module
   import math

   # Calling imported module functions
   math.sqrt(16)

   math.ceil(4.6)

   math.floor(5.7)

   ```

## `dir()` Python method
   - The dir() function returns all the properties and methods of the specified object, without the values.
   - It also returns the built-in properties which are default for a particular object.
   
   ```
   # Syntax
   dir(object)
   
   # Example
   name = "Bindesh"
   dir(name)

   ```
## Get the help about any Python object using `help()` method
   - Python help() method is used to get the documentation of specified module, class, function, variables etc. 
   - This method is generally used with python interpreter console to get details about python objects.

   ```
   # Syntax
   help(object)

   # Examples
   help(math)

   help(math.sqrt)

   help(math.pow)

   help(print)

   ```
   - You can define help() for custom classes and functions as well.

## Python Module Alias
   
   ```
   # Syntax
   import <module_name> as <alias>

   # Example-01
   import math as m

   print(m.sqrt(16))

   # Example-02
   import datetime as dnt

   print(dnt.date.today())

   ```