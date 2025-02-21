from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from app.models import *
from analyzer.tasks import *


def index(request):
    return render(request, 'index_new.html')


def result(request):
    region = request.POST.get('region')
    # 清空预测数据
    r_df = find_result_by_region(region)
    if len(r_df) != 0:
        for stamp in r_df['timestamp'].values.tolist():
            delete_result(stamp)
    # 填充预测数据
    analyze_data(region)

    # 传输数据
    df = find_result_by_region(region)
    if len(df) > 1:
        df = df.sort_values(by="year", ascending=True)
    years = df['year'].tolist()  # 年份
    line_data = df['predicted_value_field'].tolist()
    bar_data = df['predicted_value_field'].tolist()
    print(line_data)
    return render(request, 'result.html',
                  {'years': years, 'line_data': line_data, 'bar_data': bar_data, 'region': region})
