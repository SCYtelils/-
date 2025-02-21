import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import sqlite3

url = "https://data.stats.gov.cn/easyquery.htm?cn=E0103"

# 发送GET请求
response = requests.get(url, verify=False)

# 检查响应状态码
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里添加你的爬虫逻辑，提取所需的数据
    table = soup.find('table', class_='table table-bordered table-striped table-hover table-condensed table-responsive')
    if table:
        rows = table.find_all('tr')

        # 提取表头
        header = ["地区", "年份", "地区生产总值", "房地产开发企业国内贷款", "商品房销售面积", "房地产开发企业竣工房屋面积",
                  "居民消费价格指数", "房地产开发企业竣工房屋造价", "房地产开发投资额", "城镇居民可支配收入（元）",
                  "房地产开发企业土地购置费用（亿元）", "城镇人口"]

        # 提取每一行数据
        data_list = []
        for row in rows[2:]:  # 跳过表头的两行
            data = [td.text.strip() for td in row.find_all('td')]
            data_list.append(data)

        # 创建 DataFrame
        df = pd.DataFrame(data_list, columns=header)

        # 保存为CSV文件
        df.to_csv('province_data.csv', index=False, encoding='utf-8')

        # 连接到 SQLite 数据库
        conn = sqlite3.connect('houseprice.db')

        # 将数据插入到名为 data 的表中
        df.to_sql('data', conn, if_exists='replace', index=False)

        # 关闭数据库连接
        conn.close()

        print("数据已保存为 province_data.csv 文件，并插入到 houseprice.db 数据库的 data 表中")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)