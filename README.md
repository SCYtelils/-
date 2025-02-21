# -
通过机器学习预测房价，支持docker部署

# 房价预测系统

## 项目简介

本项目是一个基于 Django 框架的房价预测系统，旨在通过分析历史数据，预测未来房价趋势。系统使用了线性回归模型进行房价预测，并将预测结果可视化展示。用户可以通过输入地区名称，获取该地区的房价预测结果。

## 功能特性

- **数据管理**：支持录入、删除和查询房价相关数据。
- **房价预测**：基于线性回归模型，预测未来房价趋势。
- **结果可视化**：使用 ECharts 将预测结果以柱状图和折线图的形式展示。
- **爬虫模式**：支持通过爬虫模式自动获取网络数据。

## 技术栈

- **后端框架**：Django
- **前端框架**：Layui
- **数据可视化**：ECharts
- **机器学习模型**：Scikit-learn 的线性回归模型

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

### 2. 安装依赖

确保已安装 Python 3.x 和 pip，然后安装项目依赖：

```bash
pip install -r requirements.txt
```

### 3. 数据库迁移

在项目根目录下执行以下命令，初始化数据库：

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 运行服务器

启动 Django 开发服务器：

```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000/` 即可使用系统。

## 使用说明

1. **首页**：在首页输入地区名称，点击“立即预测”按钮，系统将根据历史数据预测该地区的房价趋势。
2. **预测结果**：预测结果将以柱状图和折线图的形式展示，用户可以直观地看到房价的变化趋势。
3. **数据管理**：通过 Django 后台管理界面，管理员可以录入、删除和查询房价相关数据。

## 数据模型

### 主要数据表

- **Data**：存储房价相关数据，包括地区、年份、GDP、企业贷款、房屋销售面积等。
- **AnalysisResult**：存储房价预测结果，包括时间戳、地区、年份、实际值、预测值和误差。
- **LprPerMonth**：存储每月的贷款市场报价利率（LPR）。


## 许可证

本项目采用 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

