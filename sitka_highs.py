import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobieranie temperatur maksymalnych z pliku.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)

    celsius_highs = [round(((row-32)*0.556), 1) for row in highs]  # Przekształcenie wyników z Farenheitów na Celsiusze
    # i zaokrąglenie do 1 miejsca po przecinku
    celsius_lows = [round(((row - 32) * 0.556), 1) for row in lows]


# Wygenerowanie wykresu najwyższych temperatur.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, celsius_highs, c='red', alpha=0.5)
ax.plot(dates, celsius_lows, c='blue', alpha=0.5)
ax.fill_between(dates, celsius_highs, celsius_lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu.
ax.set_title("Najwyższa i najniższa temperatura dnia - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (C°)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
