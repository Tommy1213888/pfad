import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file_path = 'Moon_rise_set_2024.CSV'
df = pd.read_csv(file_path)
print(df.columns)

moon_rise_times = df['RISE']
moon_set_times = df['SET']
dates = pd.to_datetime(df['YYYY-MM-DD'], format='%Y/%m/%d')

moon_rise_times = pd.to_datetime(moon_rise_times, format='%H:%M', errors='coerce')
moon_set_times = pd.to_datetime(moon_set_times, format='%H:%M', errors='coerce')

moon_rise_times = moon_rise_times.dropna()
moon_set_times = moon_set_times.dropna()

average_moon_rise = moon_rise_times.mean()
average_moon_set = moon_set_times.mean()

print(f"平均月升时间: {average_moon_rise.time()}")
print(f"平均月落时间: {average_moon_set.time()}")  #Visualize

plt.figure(figsize=(10, 6))
plt.plot(dates[:len(moon_rise_times)], moon_rise_times, label='Moon Rise', marker='o', color='blue')
plt.plot(dates[:len(moon_set_times)], moon_set_times, label='Moon Set', marker='o', color='orange')
#Set Format

plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.title('Moon Rise and Set Times')
plt.xlabel('Date')
plt.ylabel('Time (HH:MM)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() #Draw the Viz