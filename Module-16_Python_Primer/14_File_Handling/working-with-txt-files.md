# Working with `text files` using Python

In this module, you will learn how you can perform below actions on a text file using Python:
  - Open a text file
  - Read a text file
  - Traverse through a File (line-by-line)
  - Write to a text file
  - Create a new text file

## 
## [Opening a Text file using Python](https://docs.python.org/3/library/functions.html?highlight=built%20functions#open)
   
   ```
   # Opening a text file in read-only mode
   fileObj = open("samplefile.txt","r")

   ```

## Reading a Text file using Python
   
   ```
   fileObj = open("samplefile.txt","r")

   # Reading complete text file
   print(fileobj.read())

   # Reading one line at a time (starting from 1st line)
   print(fileObj.readline())

   # Read the text file by traversing through all the lines one by one
   for i in fileObj:
     print(i)

   ```

## Write to a Text file using Python
   ```
   f_obj = open('binary_file.txt',mode='w')
   
   # Get some text from user to write it in the file
   msg_to_write = input("Enter some text to write: ")

   f_obj.write(msg_to_write)

   f_obj.close()

   ```
   
## Create a Text file using Python

