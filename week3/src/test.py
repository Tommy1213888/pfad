import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

# Step 1: 爬取数据

def fetch_data(url):
    # 发送请求获取页面内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 假设你要抓取某些表格或特定标签的数据
        table = soup.find('table')  # 假设数据在 table 标签里
        data = []
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            # 检查是否为数字，并且避免空行
            if len(cols) > 1 and cols[0].isdigit() and cols[1].replace('.', '', 1).isdigit():
                data.append(cols)
        return data
    else:
        print(f"Failed to retrieve data from {url}")
        return None


# 设定要爬取的网页 URL
url = 'https://data.gov.hk/tc-data/dataset/hk-hko-rss-times-of-moonrise-moontransit-moonset/resource/96c0b176-bb6b-4680-8566-7b10c8b67e71'  # 将 URL 替换为实际的目标网页
data = fetch_data(url)

# Step 2: 分析和保存数据
if data:
    # 将抓取的数据转换为 numpy 数组
    np_data = np.array(data)

    # 假设第一列是年份，第二列是数值数据，进行数据清洗和转换
    years = np_data[:, 0].astype(int)  # 假设第一列是年份
    values = np_data[:, 1].astype(float)  # 假设第二列是数据值

    # 打印清洗后的数据
    print(f"Years: {years}")
    print(f"Values: {values}")

    # Step 3: 数据可视化
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o', color='b', label='Data')
    plt.title('Data over Time')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()
else:
    print("No data to analyze.")
