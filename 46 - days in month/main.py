def is_leap(year):
    """"
        Takes an integer value and returns
        true or false depending
        on if the year is a leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(input_year,input_month):
    """
    Takes in a year and month value and returns
    the days in that month and year
    """
    if input_month > 12 or input_month < 1:
        return "invalid input for the month (range 1-12)"
    if is_leap(input_year) and input_month == 2:
        return 29
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[input_month-1]

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)