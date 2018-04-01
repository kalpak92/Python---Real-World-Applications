## Format Date and Time Output with Strftime()

### **Step 1**

First we will see a simple step of how to format the year. It is better to understand with an example.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.9.png)](https://cdn.guru99.com/images/Pythonnew/Python15.9.png)

- We used the "**strftime function"** for formatting.
- This function uses different **control code** to give an output.
- Each control code resembles different parameters like year,month, weekday and date 
  - **[(%y/%Y – Year), (%a/%A- weekday), (%b/%B- month), (%d - day of month)] .**
  - In our case, it is **("%Y")** which resembles year, it prints out the full year with the century (e.g., 2018).

### **Step 2** 

Now if you replace ("%Y") with lowercase, i.e., ( "%y) and execute the code the output will display only (18) and not (2018). The century of the year will not display as shown in the screenshot below

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.10.png)](https://cdn.guru99.com/images/Pythonnew/Python15.10.png)

### **Step 3** 

Strf function can declare the date, day, month and year separately. Also with small changes in the control code in strftime function you can format the style of the text.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.11.png)](https://cdn.guru99.com/images/Pythonnew/Python15.11.png)

Inside the strftime function if you replace (%a) with capital A, i.e., (%A) the output will print out as "Friday" instead of just an abbreviation "Fri".

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.12.png)](https://cdn.guru99.com/images/Pythonnew/Python15.12.png)

### **Step 4** 

With the help of "strftime" function we can also retrieve local system time, date or both.

1. %C- indicates the local date and time
2. %x- indicates the local date
3. %X- indicates the local time

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.13.png)](https://cdn.guru99.com/images/Pythonnew/Python15.13.png)

In the output, you can see the result as expected

### **Step 5** 

The "strftime function" allows you to call the time in any format 24 hours or 12 hours.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.14.png)](https://cdn.guru99.com/images/Pythonnew/Python15.14.png)

Just by defining control code like %I/H for hour, % M for minute, %S for second, one can call time for different formats

**12 hours** time is declared ***[print now.strftime("%I:%M:%S %P) ]***

**24 hours** time is declared ***[print now.strftime("%H:%M")]***

```python
#
#Example file for formatting time and date output
#
from datetime import datetime
def main():
   #Times and dates can be formatted using a set of predefined string
   #Control codes
      now= datetime.now() #get the current date and time
      #%c - local date and time, %x-local's date, %X- local's time
      print(now.strftime("%c"))
      print(now.strftime("%x"))
      print(now.strftime("%X"))
##### Time Formatting ####
      #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
      print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
      print(now.strftime("%H:%M")) # 24-Hour:Minute

if __name__== "__main__":
    main()

```

