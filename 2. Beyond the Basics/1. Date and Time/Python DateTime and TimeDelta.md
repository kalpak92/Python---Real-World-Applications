# Python DateTime and TimeDelta

In Python, **date, time and datetime** classes provides a number of function to deal with dates, times and time intervals. Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps. Whenever you manipulate dates or time, you need to import datetime function.

The datetime classes in Python are categorized into main 5 classes.

- date – Manipulate just date ( Month, day, year)
- time – Time independent of the day (Hour, minute, second, microsecond)
- datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
- timedelta— A duration of time used for manipulating dates
- tzinfo— An abstract class for dealing with time zones



## How to Use Date & DateTime Class

#### **Step 1**) 

Before you run the code for datetime, it is important that you import the date time modules as shown in the screenshot below.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.1.png)](https://cdn.guru99.com/images/Pythonnew/Python15.1.png)

These import statements are pre-defined pieces of functionality in the Python library that let you manipulates dates and times, without writing any code.

Consider the following points before executing the datetime code

```
from datetime import date
```

This line tells the Python interpreter that from the datetime module import the date class We are not writing the code for this date functionality alas just importing it for our use

#### **Step 2**) 

Next, we create an instance of the date object.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.2.png)](https://cdn.guru99.com/images/Pythonnew/Python15.2.png)

#### **Step 3**) 

Next, we print the date and run the code.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.3.png)](https://cdn.guru99.com/images/Pythonnew/Python15.3.png)

The output is as expected.

## Print Date using date.today()

`date.today` function has several properties associated with it. We can print individual day/month/year and many other things

Let's see an example

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.4.png)](https://cdn.guru99.com/images/Pythonnew/Python15.4.png)

### Today's Weekday Number

The date.today() function also gives you the weekday number. Here is the Weekday Table which start with Monday as 0 and Sunday as 6

| **Day**       | **WeekDay Number** |
| ------------- | ------------------ |
| **Monday**    | 0                  |
| **Tuesday**   | 1                  |
| **Wednesday** | 2                  |
| **Thursday**  | 3                  |
| **Friday**    | 4                  |
| **Saturday**  | 5                  |
| **Sunday**    | 6                  |

Weekday Number is useful for arrays whose index is dependent on the Day of the week.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.5.png)](https://cdn.guru99.com/images/Pythonnew/Python15.5.png)



## Python Current Date and Time: now() today()

#### **Step 1)** 

Like Date Objects, we can also use **"DATETIME OBJECTS"** in Python. It gives date along with time in **hours, minutes, seconds and milliseconds.**

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.6.png)](https://cdn.guru99.com/images/Pythonnew/Python15.6.png)

When we execute the code for datetime, it gives the output with current date and time.

#### **Step 2)** 

With "DATETIME OBJECT", you can also call time class.

Suppose we want to print just the current time without the date.

```python
t = datetime.time(datetime.now())
```

- We had imported the time class. We will be assigning it the current value of time using datetime.now()
- We are assigning the value of the current time to the variable t.

And this will give me just the time. So let's run this program.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.7.png)](https://cdn.guru99.com/images/Pythonnew/Python15.7.png)

Okay, so you can see that here I got the date and time. And then the next line, I've got just the time by itself

#### **Step 3)** 

We will apply our weekday indexer to our weekday's arrayList to know which day is today

- Weekdays operator (wd) is assigned the number from (0-6) number depending on what the current weekday is. Here we declared the array of the list for days (Mon, Tue, Wed…Sun).
- Use that index value to know which day it is. In our case, it is #2, and it represents Wednesday, so in the output it will print out "Which is a Wednesday."

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.8.png)](https://cdn.guru99.com/images/Pythonnew/Python15.8.png)

Here is the complete code to get current date and time using datetime now:

```python
from datetime import date
from datetime import time
from datetime import datetime
def main():
    ##DATETIME OBJECTS
    #Get today's date from datetime class
    today=datetime.now()
    #print (today)
    # Get the current time
    #t = datetime.time(datetime.now())
    #print "The current time is", t
    #weekday returns 0 (monday) through 6 (sunday)
    wd=date.weekday(today)
    #Days start at 0 for monday
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

if __name__== "__main__":
    main()
```

## Complete List of Datetime Formatting Codes

| Code  | Meaning                                                      | Example                    |
| ----- | ------------------------------------------------------------ | -------------------------- |
| `%a`  | Weekday as locale’s abbreviated name.                        | `Mon`                      |
| `%A`  | Weekday as locale’s full name.                               | `Monday`                   |
| `%w`  | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. | `1`                        |
| `%d`  | Day of the month as a zero-padded decimal number.            | `30`                       |
| `%-d` | Day of the month as a decimal number. (Platform specific)    | `30`                       |
| `%b`  | Month as locale’s abbreviated name.                          | `Sep`                      |
| `%B`  | Month as locale’s full name.                                 | `September`                |
| `%m`  | Month as a zero-padded decimal number.                       | `09`                       |
| `%-m` | Month as a decimal number. (Platform specific)               | `9`                        |
| `%y`  | Year without century as a zero-padded decimal number.        | `13`                       |
| `%Y`  | Year with century as a decimal number.                       | `2013`                     |
| `%H`  | Hour (24-hour clock) as a zero-padded decimal number.        | `07`                       |
| `%-H` | Hour (24-hour clock) as a decimal number. (Platform specific) | `7`                        |
| `%I`  | Hour (12-hour clock) as a zero-padded decimal number.        | `07`                       |
| `%-I` | Hour (12-hour clock) as a decimal number. (Platform specific) | `7`                        |
| `%p`  | Locale’s equivalent of either AM or PM.                      | `AM`                       |
| `%M`  | Minute as a zero-padded decimal number.                      | `06`                       |
| `%-M` | Minute as a decimal number. (Platform specific)              | `6`                        |
| `%S`  | Second as a zero-padded decimal number.                      | `05`                       |
| `%-S` | Second as a decimal number. (Platform specific)              | `5`                        |
| `%f`  | Microsecond as a decimal number, zero-padded on the left.    | `000000`                   |
| `%z`  | UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive). |                            |
| `%Z`  | Time zone name (empty string if the object is naive).        |                            |
| `%j`  | Day of the year as a zero-padded decimal number.             | `273`                      |
| `%-j` | Day of the year as a decimal number. (Platform specific)     | `273`                      |
| `%U`  | Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | `39`                       |
| `%W`  | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | `39`                       |
| `%c`  | Locale’s appropriate date and time representation.           | `Mon Sep 30 07:06:05 2013` |
| `%x`  | Locale’s appropriate date representation.                    | `09/30/13`                 |
| `%X`  | Locale’s appropriate time representation.                    | `07:06:05`                 |
| `%%`  | A literal '%' character.                                     | `%`                        |

Note: Examples are based on `datetime.datetime(2013, 9, 30, 7, 6, 5)`



## [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) Objects

A [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object represents a duration, the difference between two dates or times.

*class* `datetime.``timedelta`(*days=0*, *seconds=0*, *microseconds=0*, *milliseconds=0*, *minutes=0*, *hours=0*, *weeks=0*)

All arguments are optional and default to `0`. Arguments may be integers or floats, and may be positive or negative.

Only *days*, *seconds* and *microseconds* are stored internally. Arguments are converted to those units:

- A millisecond is converted to 1000 microseconds.
- A minute is converted to 60 seconds.
- An hour is converted to 3600 seconds.
- A week is converted to 7 days.

and days, seconds and microseconds are then normalized so that the representation is unique, with

- `0 <= microseconds < 1000000`
- `0 <= seconds < 3600*24` (the number of seconds in one day)
- `-999999999 <= days <= 999999999`

If any argument is a float and there are fractional microseconds, the fractional microseconds left over from all arguments are combined and their sum is rounded to the nearest microsecond using round-half-to-even tiebreaker. If no argument is a float, the conversion and normalization processes are exact (no information is lost).

If the normalized value of days lies outside the indicated range, [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError) is raised.

Note that normalization of negative values may be surprising at first. For example,

```python
>>> from datetime import timedelta
>>> d = timedelta(microseconds=-1)
>>> (d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)
```

- `timedelta.``min`

  The most negative [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object, `timedelta(-999999999)`.


- `timedelta.``max`

  The most positive [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object, `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`.


- `timedelta.``resolution`

  The smallest possible difference between non-equal [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) objects, `timedelta(microseconds=1)`.

Note that, because of normalization, `timedelta.max` > `-timedelta.min`. `-timedelta.max` is not representable as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object.

Instance attributes (read-only):

| Attribute      | Value                                      |
| -------------- | ------------------------------------------ |
| `days`         | Between -999999999 and 999999999 inclusive |
| `seconds`      | Between 0 and 86399 inclusive              |
| `microseconds` | Between 0 and 999999 inclusive             |

Supported operations:

| Operation                         | Result                                                       |
| --------------------------------- | ------------------------------------------------------------ |
| `t1 = t2 + t3`                    | Sum of *t2* and *t3*. Afterwards *t1*-*t2* == *t3* and *t1*-*t3* == *t2* are true. (1) |
| `t1 = t2 - t3`                    | Difference of *t2* and *t3*. Afterwards *t1* == *t2* - *t3* and *t2* == *t1* + *t3* are true. (1) |
| `t1 = t2 * i or t1 = i * t2`      | Delta multiplied by an integer. Afterwards *t1* // i == *t2* is true, provided `i != 0`. |
|                                   | In general, *t1* * i == *t1* * (i-1) + *t1* is true. (1)     |
| `t1 = t2 * f or t1 = f * t2`      | Delta multiplied by a float. The result is rounded to the nearest multiple of timedelta.resolution using round-half-to-even. |
| `f = t2 / t3`                     | Division (3) of *t2* by *t3*. Returns a [`float`](https://docs.python.org/3/library/functions.html#float) object. |
| `t1 = t2 / f or t1 = t2 / i`      | Delta divided by a float or an int. The result is rounded to the nearest multiple of timedelta.resolution using round-half-to-even. |
| `t1 = t2 // i` or `t1 = t2 // t3` | The floor is computed and the remainder (if any) is thrown away. In the second case, an integer is returned. (3) |
| `t1 = t2 % t3`                    | The remainder is computed as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object. (3) |
| `q, r = divmod(t1, t2)`           | Computes the quotient and the remainder: `q = t1 // t2` (3) and `r = t1 % t2`. q is an integer and r is a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object. |
| `+t1`                             | Returns a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object with the same value. (2) |
| `-t1`                             | equivalent to [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta)(-*t1.days*, -*t1.seconds*, -*t1.microseconds*), and to *t1** -1. (1)(4) |
| `abs(t)`                          | equivalent to +*t* when `t.days >= 0`, and to -*t* when `t.days < 0`. (2) |
| `str(t)`                          | Returns a string in the form `[D day[s], ][H]H:MM:SS[.UUUUUU]`, where D is negative for negative `t`. (5) |
| `repr(t)`                         | Returns a string in the form `datetime.timedelta(D[, S[, U]])`, where D is negative for negative `t`. (5) |

Notes:

1. This is exact, but may overflow.

2. This is exact, and cannot overflow.

3. Division by 0 raises [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

4. -*timedelta.max* is not representable as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) object.

5. String representations of [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) objects are normalized similarly to their internal representation. This leads to somewhat unusual results for negative timedeltas. For example:

   \>>>

   ```
   >>> timedelta(hours=-5)
   datetime.timedelta(-1, 68400)
   >>> print(_)
   -1 day, 19:00:00
   ```

In addition to the operations listed above [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) objects support certain additions and subtractions with [`date`](https://docs.python.org/3/library/datetime.html#datetime.date) and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) objects (see below).

## How to use Timedelta Objects

**With timedelta objects, you can estimate the time for both future and the past.** In other words, it is a timespan to predict any special day, date or time.

**Remember this function is not for printing out the time or date, but something to CALCULATE about the future or past**. Let's see an example to understand it better.

### **Step 1)** 

To run Timedelta Objects, you need to declare the import statement first and then execute the code

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.15.png)](https://cdn.guru99.com/images/Pythonnew/Python15.15.png)

1. Write import statement for timedelta
2. Now write the code to print out object from time delta as shown in screen shot
3. Run the code. The timedelta represents a span of 365 days, 8 hrs and 15 minutes and prints the same

Confusing? Next step will help-

### **Step 2)** 

Let's get today's date and time to check whether our import statement is working well. When code is executed, it prints out today's date which means our import statement is working well

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.16.png)](https://cdn.guru99.com/images/Pythonnew/Python15.16.png)

### **Step 3)** 

We will see how we can retrieve date a year from now through delta objects. When we run the code, it gives the output as expected.

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.17.png)](https://cdn.guru99.com/images/Pythonnew/Python15.17.png)

### **Step 4)** 

Another example of how time delta can be used to calculate future date from current date and time

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.18.png)](https://cdn.guru99.com/images/Pythonnew/Python15.18.png)

### **Step 5)** 

Let's look into a more complex example. I would like to determine how many days past the New Year. Here is how we will proceed

- Using today= date.today() we will get todays date
- We know the newyear is always on 1-Jan, but the year could be different. Using nyd= date(today.year,1,1) we store the new year in variable nyd
- if nyd < today: compares whether the current date is greater than the new year. If yes, it enters the while loop
- ((today-nyd).days) gives the difference between a current date and new year in DAYS

[![Python Date & Time Tutorial: Timedelta, Datetime, & Strftime](https://cdn.guru99.com/images/Pythonnew/Python15.19.png)](https://cdn.guru99.com/images/Pythonnew/Python15.19.png)

The output shows that "New Year Day already went by 11 days ago."

```python
#
# Example file for working with timedelta objects
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print (timedelta(days=365, hours=8, minutes=15))
# print today's date
print ("today is: " + str(datetime.now()))
# print today's date one year from now
print ("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))
# create a timedelta that uses more than one argument
# print (in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))
# How many days until New Year's Day?
today = date.today()  # get todays date
nyd = date(today.year, 1, 1)  # get New Year Day for the same year
# use date comparison to see if New Year Day has already gone for this year
# if it has, use the replace() function to get the date for next year
if nyd < today:
    print ("New Year day is already went by %d days ago" % ((today - nyd).days))
```

## Summary

For manipulating dates and times in both simple and complex ways datetime module supplies different classes or categories like

- date – Manipulate just date ( Month, day, year)
- time – Time independent of the day (Hour, minute, second, microsecond)
- datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
- timedelta— A duration of time used for manipulating dates
- tzinfo— An abstract class for dealing with timezones

#### **Using datetime objects**

- Importing datetime objects before executing the code is mandatory
- Using date.today function for printing individual date/month/year as well as indexing the day
- Using date.time object to get time in hours, minutes, seconds and milliseconds

#### **Timedelta Objects**

- With timedelta objects, you can estimate the time for both future and the past
- Calculate the total days left for the special day(birthday) from the current time
- Calculate the total days passed for special day(birthday) from the current time

