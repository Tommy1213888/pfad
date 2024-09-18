import requests23
from lxml import html
import dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载环境变量
dotenv.load_dotenv()

# 定义 URL 和文件名
url = os.getenv('CO2_URL', 'https://unstats.un.org/unsd/envstats/unsd_co2_emissions.xlsx')
filename = os.getenv('FILENAME', 'co2_emissions.xlsx')


# Step 1: 下载数据或读取本地文件
def download_data(url, filename):
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'{filename} downloaded successfully.')
    else:
        print(f'{filename} already exists.')


download_data(url, filename)


# Step 2: 读取 Excel 文件并转换为 Pandas DataFrame
def read_excel_data(filename):
    df = pd.read_excel(filename, sheet_name=0)  # 假设数据在第一个表格中
    print("Data loaded successfully.")
    return df


df = read_excel_data(filename)


# Step 3: 筛选出特定国家的数据
def filter_country_data(df, country):
    country_data = df[df['Country'] == country]
    country_data = country_data[['Year', 'CO2 Emissions']]  # 假设有 "Year" 和 "CO2 Emissions" 列
    return country_data


# 选择要分析的国家，例如中国
country = 'China'
china_data = filter_country_data(df, country)

print(china_data.head())


# Step 4: 数据可视化（绘制二氧化碳排放量时间序列图）
def plot_data(country_data, country):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='CO2 Emissions', data=country_data, marker='o', color='b')
    plt.title(f'CO2 Emissions Over Time in {country}', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('CO2 Emissions (Million Metric Tons)', fontsize=14)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_data(china_data, country)


# Step 5: 比较多个国家的 CO2 排放量
def compare_countries(df, countries):
    plt.figure(figsize=(12, 8))
    for country in countries:
        country_data = filter_country_data(df, country)
        sns.lineplot(x='Year', y='CO2 Emissions', data=country_data, label=country, marker='o')

    plt.title('CO2 Emissions Comparison Between Countries', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('CO2 Emissions (Million Metric Tons)', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 比较中国、美国和印度的排放量
compare_countries(df, ['China', 'United States', 'India'])
