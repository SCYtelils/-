import uuid

from background_task import background
from sklearn.linear_model import LinearRegression
import pandas as pd
from analyzer.models import *


def analyze_data(region):

    # 读取数据
    data = find_data_by_region(region)
    data = data.drop(['sold_area', 'completed_area'], axis=1)

    # 提取训练数据
    train_x = data.iloc[:, 3:12]
    train_y = data.iloc[:, 12]

    # 拟合模型
    model = LinearRegression()
    model.fit(train_x, train_y)

    predicted_y = model.predict(train_x)
    data['Predicted Price'] = predicted_y

    # 提取需要的列数据
    selected_columns = ['year', 'house_price', 'Predicted Price', 'region']
    new_df = data[selected_columns].copy()

    # 将"house_price"的列名替换为"actual_value"
    new_df.rename(columns={'house_price': 'actual_value', 'Predicted Price': 'predicted_value'}, inplace=True)
    new_df.insert(new_df.columns.get_loc('region'), 'prediction_error', 0)

    new_df.insert(new_df.columns.get_loc('year'), 'timestamp', new_df.index + 1)

    result_list = new_df.values.tolist()

    print(new_df)

    for r in result_list:
        k = generate_unique_key()
        checker = insert_result(k, r[1], r[4], r[3], r[2], r[5])
        print(checker)


def generate_unique_key():
    key = str(uuid.uuid4())
    return key
