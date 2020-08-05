"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import date

## Old Code

# year = date.today().year
# month = date.today().month

# args_len = len(sys.argv)

# # If no args were given.

# if args_len == 1:

#   print(calendar.month(year,month))

# else:

#   try:

#     # If two arg were given.

#     if args_len == 2:

#       if len(sys.argv[1]) < 3:
#         month = int('0' + str(sys.argv[1][1]))

#       else:
#         month = int(sys.argv[1][1:3])

#       print(calendar.month(year,month))

#     elif args_len == 3:

#       if len(sys.argv[1]) < 4:
#         month = int('0' + str(sys.argv[1][1]))

#       else:
#         month = int(sys.argv[1][1:3])
      
#       year = int(sys.argv[2][1:5])

#       print(calendar.month(year,month))

#     else:

#       print('The correct format is script_name.py [month_number] [year_number]')

#   except:

#     print('The correct format is script_name.py [month_number] [year_number]')

## New Code

year = date.today().year
month = date.today().month

args_len = len(sys.argv)

# If no args were given.

if args_len == 1:

  print(calendar.month(year,month))

else:

  try:

    # If two arg were given.

    if args_len == 2:

      month = int(sys.argv[1])

      print(calendar.month(year,month))

    elif args_len == 3:

      month = int(sys.argv[1])
      
      year = int(sys.argv[2][0:5])

      if len(sys.argv[2]) < 4:
        print(f'Notice your getting {sys.argv[2]} AD, otherwise enter the full year.')
      print(calendar.month(year,month))

    else:

      print('The correct format is script_name.py [month_number] [year_number]')

  except:

    print('The correct format is script_name.py [month_number] [year_number]')

