import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 加载CSV文件数据
file_path = r'C:\Users\15950\Desktop\Python_Projects\Luo_Yiyan\assignment\Moon_rise_set_2024.CSV'  # 替换为实际的文件路径
df = pd.read_csv(file_path)  # 使用 read_csv() 读取 CSV 文件

# 打印CSV文件中的列名，确认实际的列名称
print(df.columns)

# 提取月升和月落时间数据，列名为 'RISE' 和 'SET'
moon_rise_times = df['RISE']
moon_set_times = df['SET']
dates = pd.to_datetime(df['YYYY-MM-DD'], format='%Y/%m/%d')

# 转换时间为 datetime 格式，方便处理
moon_rise_times = pd.to_datetime(moon_rise_times, format='%H:%M', errors='coerce')
moon_set_times = pd.to_datetime(moon_set_times, format='%H:%M', errors='coerce')

# 过滤无效时间
moon_rise_times = moon_rise_times.dropna()
moon_set_times = moon_set_times.dropna()

# 计算平均月升和月落时间
average_moon_rise = moon_rise_times.mean()
average_moon_set = moon_set_times.mean()

print(f"平均月升时间: {average_moon_rise.time()}")
print(f"平均月落时间: {average_moon_set.time()}")

# 数据可视化：绘制月升和月落时间的折线图
plt.figure(figsize=(10, 6))
plt.plot(dates[:len(moon_rise_times)], moon_rise_times, label='Moon Rise', marker='o', color='blue')
plt.plot(dates[:len(moon_set_times)], moon_set_times, label='Moon Set', marker='o', color='orange')

# 设置纵轴格式为 HH:MM 时间
plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.title('Moon Rise and Set Times')
plt.xlabel('Date')
plt.ylabel('Time (HH:MM)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
