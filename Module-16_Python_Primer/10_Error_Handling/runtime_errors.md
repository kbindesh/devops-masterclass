# Python runtime errors

## Example-01 of runtime error
   ```
    num = int(input('Enter numerator'))
    deno = int(input('Enter denominator'))
    
    result = num/deno
    print(result)
   ```

## Example-02 of runtime error
   ```
    even_numbers = [2,4,6,8]
    try:
        print(even_numbers[5])
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except IndexError:
        print("Index Out of Bound error has occured.")
   ```