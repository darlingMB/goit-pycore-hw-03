from datetime import datetime, timedelta



users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {'name': 'Test_name', 'birthday': '2003.10.13'}
]

def get_upcoming_birthdays(users):
    
    upcoming_birthdays = []

    current_date = datetime.today().date()

    for user in users:
        user_name = user['name']
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = user_birthday.replace(year = current_date.year)
        
        if  birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year = current_date.year + 1)
        
        days_to_birthday = (birthday_this_year - current_date).days
        
        if 0 <= days_to_birthday <= 7:
            if birthday_this_year.weekday in [5, 6]:
                days_to_monday = 7 - birthday_this_year + timedelta(days = days_to_monday)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append(
                {
                "name": user_name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                }
            )
        
        
    return upcoming_birthdays










def main():
    upcoming_birthdays = get_upcoming_birthdays(users=users)
    print("Список привітань на цьому тижні:\n",upcoming_birthdays)




if __name__ == '__main__':
    main()