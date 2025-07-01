import pandas as pd
import datetime
import calendar

# Get the current date and time
current_datetime = pd.Timestamp.now()
print("1. Current Date and Time:", current_datetime)

# Get the day of the week
day_of_week = current_datetime.day_name()
print("2. Day of the Week:", day_of_week)

# Get the day of the year
day_of_year = current_datetime.day_of_year
print("3. Day of the Year:", day_of_year)

# Get the number of days in the current month
_, num_days_in_month = calendar.monthrange(current_datetime.year, current_datetime.month)
print("4. Number of Days in This Month:", num_days_in_month)

# Check if the year is a leap year
is_leap = calendar.isleap(current_datetime.year)
print("5. Is Leap Year:", is_leap)

# Check if the date is the last day of the month
is_last_day_of_month = current_datetime.day == num_days_in_month
print("6. Is Last Day of the Month:", is_last_day_of_month)

# Check if the date is the first day of the month
is_first_day_of_month = current_datetime.day == 1
print("7. Is First Day of the Month:", is_first_day_of_month)

# Check if the date is the last day of the year
is_last_day_of_year = current_datetime.month == 12 and current_datetime.day == 31
print("8. Is Last Day of the Year:", is_last_day_of_year)

# Check if the date is the first day of the year
is_first_day_of_year = current_datetime.month == 1 and current_datetime.day == 1
print("9. Is First Day of the Year:", is_first_day_of_year)
