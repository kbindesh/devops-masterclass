# Working with Files using Python

In this module, you will learn how you can perform below actions on a text file using Python:
  - Import .csv module
  - Open a .csv file
  - Read a .csv file
  - Write to a text file
  - Create a new text file

## [Import the `.csv module`](https://docs.python.org/3/library/csv.html)
   
   ```
   import csv

   ```
## Syntax
   
   ```
   # open a file
   file_obj = open('file_name','mode',buffer)

   # close a file
   file_obj.close()
   ```
## File processing mode
   - r: read 
   - w: write
   - a: append
   - w+: read and write
   - r+: read, write and append
   - a+: append and read
   - x: exclusive creation mode (create a new file and open it | if already exist, will throw error )
   
## [Open a `.csv file`](https://docs.python.org/3/library/functions.html?highlight=built%20functions#open)
   
   ```
   import csv

   # Opening a .csv file in read-only mode
   fileObj = open("samplefile.csv","r")

   ```

## [Read a `.csv file`]()
   
   ```
   # Import the csv module
   import csv

   # Open a csv file
   file_obj = open("samplecsvfile.csv","r")
   print(file_obj)

   # Read the csv file
   file_rdr = csv.reader(file_obj,delimiter=",")

   # Display the file contents of opened csv file
   for row in file_rdr:
      print(row)
   
   ```

## [Close a `.csv file`]()

   ```
   # Import the csv module
   import csv

   # Open a .csv file in read-only mode
   fileObj = open("samplefile.csv","r")

   # Close a .csv file
   fileObj.close()
   
   ```
## [Write to a .csv file]()
   
   ```
   # Import the csv module
   import csv

   # Define a new row contents to be added to the existing csv file
   newRow = ["200", "Bindesh", "Python", "C13453"]
   
   # Open an existing csv file to write into it
   fileObj = open("samplefile.csv","a")

   # Define the csv writer object
   wrt_obj = csv.writer(fileObj)

   # Write to csv file
   write_obj.writerow(newRow)

   # Close the csv file
   file.close()

   ```

## [Read the subset of records (csv file) based on filter criteria]()
   
   ```
   
   ```