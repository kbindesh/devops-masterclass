# Python's Module, Package and Library

## 1. What is `Module` in Python?
   - The `module` is a basically a bunch of related code saved in a Python file that contains collections of `functions`,`classes` and  `variables`.
   - Modules are with `.py` extension file. 
   - It is an executable file and to organize all the modules, we have the concept called Package in Python. 

### Examples of Python Modules
   1) Datetime
   2) regex
   3) random
   4) html
   5) re

## 2. What is `Package` in Python?
   - The `package` is a simple directory having collections of modules.
   - This directory may contain Python modules and also have __init__.py file by which the interpreter interprets it as a `Package`. 
   - The package is simply a namespace.
   - The package also contains sub-packages inside it. 

### Examples of Python Package
   - Numpy 
   - Pandas

   ```
   Employee(Package)
    | __init__.py (Constructor)
    | emp_details.py (Module)
    | performance.py (Module)
    | project_details.py (Module)
    | other_contributions.py (Module)
   ```

## 3. What is `Library` in Python?
   - The `library` is a collection of related functionality of codes that allows you to perform many tasks without writing your code. 
   - Python library is a reusable chunk of code that we can use by importing it into our program.
   - You can use it by importing the library and calling the method of that library with a period(.). 
   - It is often assumed that while a package is a collection of modules, a library is a collection of packages.

### Examples of Python Libraries
   - Seaborn
   - Matplotlib
   - PyTorch
   - NumPy
   
   ```
   import pandas as pd
 
   df = pd.read_csv("customer_accounts.csv")
    
   ```

## 4. What are Python Frameworks?
   - Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to fast track the development process. 
   - However, frameworks are usually more complex than libraries. 
   - Also, while libraries contain packages that perform specific operations, frameworks contain the basic flow and architecture of the application.

### Some popular Python frameworks
   - Django
   - Flask
   - Bottle