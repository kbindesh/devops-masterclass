# Python datetime module

## Overview
   - Python Datetime module supplies classes to work with date and time. 
   - These classes provide a number of functions to deal with dates, times, and time intervals.
   - The DateTime module is categorized into six main classes:
     - date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month, and day.
     - time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.
     - datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
     - timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
     - tzinfo – It provides time zone information objects.
     - timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC.

### Python Date class Syntax
   ```
   class datetime.date(year, month, day)
   ```
### Example: Get the Current Date
   ```
   from datetime import date
   date.today()
   
   OR
   
   import datetime

   todays_date = datetime.date.today()
   print(todays_date)

   ```
### Get Today’s Year, Month, and Date
   ```
    from datetime import date

    # date object of today's date
    today = date.today()

    print("Current year:", today.year)
    print("Current month:", today.month)
    print("Current day:", today.day)

   ```
### Get current time
   ```
   import datetime
   
   current_time = datetime.datetime.now()
   print(current_time)
   ```