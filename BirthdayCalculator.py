from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()

    # Split the birthdate into year, month, and day
    birth_year, birth_month, birth_day = map(int, birthdate.split('-'))

    # Create a birthdate datetime object for comparison
    birth_date_obj = datetime(birth_year, birth_month, birth_day)

    # Calculate age
    age_year = today.year - birth_year
    age_month = today.month - birth_month
    age_day = today.day - birth_day

    # If the birth day hasn't occurred this month yet, subtract one month
    if age_day < 0:
        age_month -= 1
        age_day += 30  # This is a simplification; some months have 31 days, February might have 28 or 29.

    # If the birth month hasn't occurred this year yet, subtract one year
    if age_month < 0:
        age_year -= 1
        age_month += 12

    return age_year, age_month, age_day

def main():
    birthdate = input("Enter your birthdate in YYYY-MM-DD format: ")
    years, months, days = calculate_age(birthdate)
    print(f"You are {years} years, {months} months, and {days} days old.")

if __name__ == "__main__":
    main()
