import csv
from datetime import datetime
from matplotlib import pyplot as plt
import os

while True:
    print("\nMenu:\n1. Highs\n2. Lows\n3. Exit")
    choice = input("Please choose an option (1, 2, 3): ")

    if choice == '1' or choice == '2':
        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, temps = [], []
            for row in reader:
                current_date = datetime.strptime(row[2],
                '%Y-%m-%d')
                dates.append(current_date)

                # Get the temperature based on user choice
                temp_index = 5 if choice == '1' else 6
                temp = int(row[temp_index])
                temps.append(temp)


            # Plot temperatures
            fig, ax = plt.subplots()
            ax.plot(dates, temps, c= 'red' if choice == '1' else 'blue')

            # Format plot
        title = "Daily high temperatures  -  2018" if choice == '1' else "Daily low temperatures  -  2018"
        plt.title(title, fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '3':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please choose among 1, 2 and 3.")
