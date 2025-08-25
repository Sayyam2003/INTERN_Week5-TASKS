from datetime import datetime, date

def days_until_birthday(month: int, day: int):
    today = date.today()
    current_year = today.year
    birthday_this_year = date(current_year, month, day)

    # If birthday has already passed this year, calculate for next year
    if birthday_this_year < today:
        birthday_next = date(current_year + 1, month, day)
    else:
        birthday_next = birthday_this_year

    delta = birthday_next - today
    return delta.days

# Example: Set your birthday (month, day)
my_birthday_month = 10
my_birthday_day = 27

days_left = days_until_birthday(my_birthday_month, my_birthday_day)
print(f"🎉 {days_left} days until your next birthday!")

#Output
🎉 63 days until your next birthday!