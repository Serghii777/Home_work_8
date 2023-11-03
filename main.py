from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = date.today()

    # Ініціалізуємо словник для зберігання користувачів на кожний день тижня
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }
    if not users :
        return {}

    for user in users:
        birthday_this_year = current_date.replace(month=user['birthday'].month, day=user['birthday'].day)
        if birthday_this_year < current_date:
            birthday_this_year = current_date.replace(year=current_date.year + 1, month=user['birthday'].month,
                                                  day=user['birthday'].day)

        if current_date <= birthday_this_year <= current_date + timedelta(days=6):

            day_of_week = birthday_this_year.strftime('%A')
            if day_of_week in ('Sunday', 'Sataday'):
                birthdays_per_week.get('Monday').append(user['name'])
            else:
                birthdays_per_week.get(day_of_week).append(user['name'])


    return  {day: name for day, name in birthdays_per_week.items() if name}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
