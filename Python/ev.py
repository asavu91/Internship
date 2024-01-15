def calculate_range():
    battery_cap = 62
    energy_consumption = 15.6
    battery_level_input = int(input("Insert current battery level:"))

    if battery_level_input <= battery_cap and battery_level_input > 0:
        battery_level = (100 * battery_level_input) / 62
        procentage_battery_level = (battery_cap * battery_level) / 100
        estimated_range = round((procentage_battery_level / energy_consumption) * 100)
        print(str(estimated_range) + " Km")
    else:
        print("Please insert a number between 1 and 62")


calculate_range()
