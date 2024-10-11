from datetime import datetime


def get_days_from_today(date):
    try:
        number_of_days = datetime.now() - datetime.strptime(date, "%Y-%m-%d")

        return number_of_days.days
        
    except:
        print('Incorrect format of date')

    




def main():
    while True:
        result = get_days_from_today(date=input("Please enter a date in format year-month-day(2024-10-01): "))
        
        if result is not None:
            print(result)
            break
    

if __name__ == "__main__":
    main()