from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(birthdate):
    today = datetime.today()

    # Split the birthdate into year, month, and day
    birth_year, birth_month, birth_day = map(int, birthdate.split('-'))

    # Create a birthdate datetime object for comparison
    birth_date_obj = datetime(birth_year, birth_month, birth_day)

    # Calculate the difference in years, months, and days using relativedelta
    delta = relativedelta(today, birth_date_obj)
    age_year = delta.years
    age_month = delta.months
    age_day = delta.days

    return age_year, age_month, age_day

def main():
    birthdate = input("Enter your birthdate in YYYY-MM-DD format: ")
    years, months, days = calculate_age(birthdate)
    print(f"You are {years} years, {months} months, and {days} days old.")

if __name__ == "__main__":
    main()
