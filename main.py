from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    day_now = date.today() # Отримую сьогоднішню дату
    next_week = day_now + timedelta(days=7) # Отримую наступний тиждень

    # Словник з днями тижня і назвами
    days_name = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    # Створюю словник для днів народження
    weeks_users = {day: [] for day in days_name.values()}

    for user in users:
        # Якщо відсутн'є ім'я дивимось список далі
        if user["name"] == "":
            continue

        # Отримую дату народження
        date_of_birth = user["birthday"].replace(year=day_now.year)
        # Якщо день народження в цьому році вже був
        if date_of_birth < day_now:
            date_of_birth = date_of_birth.replace(year=day_now.year + 1)

        if day_now <= date_of_birth <= next_week:
            # Робочі дні
            day_name = days_name[date_of_birth.weekday()] 
            # Перевірка перенесення дня народження з вихідних на понеділок
            if day_name in ["Saturday", "Sunday"]:
                day_name = "Monday"
            # Заповнюю список назвою тижня та іменами співробітників
            weeks_users[day_name].append(user["name"])

    return {day: names for day, names in weeks_users.items() if names}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")