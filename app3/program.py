import datetime

def print_header():
    print('---------------------')
    print('    BIRTHDATE APP')
    print('---------------------')
    print()

def get_birthdate_from_user():
    year = int(input('What year where you born [YYYY]: '))
    month = int(input('What month where you born [MM]: '))
    day = int(input('What day where you born [DD]: '))
    return datetime.date(year, month, day)

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(
        target_date.year, original_date.month, original_date.day)
    delta = this_year - target_date
    return delta.days

def print_birthdate_information(days):
    if days > 0:
        print('Your birthday is in {} days!'.format(days))
    elif days < 0:
        print('You had your birthday {} days ago this year'.format(-days))
    else:
        print('Happy birthday!!!')

def main():
    print_header()
    bday = get_birthdate_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthdate_information(number_of_days)

main()
