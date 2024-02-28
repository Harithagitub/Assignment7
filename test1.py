def get_season(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
    season_index = (month % 12 + 3) // 3
    return seasons[season_index]

user_input = input("Enter the number of a month (1-12): ")

try:
    month_number = int(user_input)
    season = get_season(month_number)
    print(f"The season for month {month_number} is {season}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")