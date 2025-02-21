# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import pandas as pd


class LprPerMonth(models.Model):
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    lpr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LPR_per_month'


class AnalysisResult(models.Model):
    timestamp = models.TextField(primary_key=True, blank=True, null=False)
    region = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    actual_value_field = models.FloatField(db_column='actual_value ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    predicted_value_field = models.FloatField(db_column='predicted_value ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    prediction_error = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_result'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BackgroundTask(models.Model):
    task_name = models.CharField(max_length=190)
    task_params = models.TextField()
    task_hash = models.CharField(max_length=40)
    verbose_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    run_at = models.DateTimeField()
    repeat = models.BigIntegerField()
    repeat_until = models.DateTimeField(blank=True, null=True)
    queue = models.CharField(max_length=190, blank=True, null=True)
    attempts = models.IntegerField()
    failed_at = models.DateTimeField(blank=True, null=True)
    last_error = models.TextField()
    locked_by = models.CharField(max_length=64, blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    creator_object_id = models.PositiveIntegerField(blank=True, null=True)
    creator_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'background_task'


class BackgroundTaskCompletedtask(models.Model):
    task_name = models.CharField(max_length=190)
    task_params = models.TextField()
    task_hash = models.CharField(max_length=40)
    verbose_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    run_at = models.DateTimeField()
    repeat = models.BigIntegerField()
    repeat_until = models.DateTimeField(blank=True, null=True)
    queue = models.CharField(max_length=190, blank=True, null=True)
    attempts = models.IntegerField()
    failed_at = models.DateTimeField(blank=True, null=True)
    last_error = models.TextField()
    locked_by = models.CharField(max_length=64, blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    creator_object_id = models.PositiveIntegerField(blank=True, null=True)
    creator_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'background_task_completedtask'


class Data(models.Model):
    region = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    gdp = models.FloatField(blank=True, null=True)
    company_loan = models.FloatField(blank=True, null=True)
    sold_area = models.FloatField(blank=True, null=True)
    completed_area = models.FloatField(blank=True, null=True)
    consumption_index = models.FloatField(blank=True, null=True)
    house_cost = models.FloatField(blank=True, null=True)
    investment = models.FloatField(blank=True, null=True)
    residents_income = models.FloatField(blank=True, null=True)
    land_cost = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)
    lpr = models.FloatField(blank=True, null=True)
    house_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


def find_all_data():
    """
    查找data表中所有数据
    :return: Dataframe
    """
    queryset = Data.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_data_by_region(region_name):
    """
    按地名查找数据
    :param region_name: 地名 字符串
    :return: Dataframe
    """
    queryset = Data.objects.filter(region=region_name)
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_data_by_year(y):
    """
    按年份查找数据
    :param y: 年 整型
    :return: Dataframe
    """
    queryset = Data.objects.filter(year=y)
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_data(reg, y):
    """
    条件查找数据
    :param reg: 地区 字符串
    :param y: 年份 整型
    :return: Dataframe
    """
    queryset = Data.objects.filter(year=y, region=reg)
    df = pd.DataFrame(list(queryset.values()))
    return df

def find_all_result():
    """
    查找所有分析结果数据
    :return: Dataframe
    """
    queryset = AnalysisResult.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_result_by_year(y):
    """
    按年份查找分析结果
    :param y: 年 整型
    :return: Dataframe
    """
    queryset = AnalysisResult.objects.filter(year=y)
    df = pd.DataFrame(list(queryset.values()))
    return df

def find_result_by_region(region):
    """
    按年份查找分析结果
    :param y: 年 整型
    :return: Dataframe
    """
    queryset = AnalysisResult.objects.filter(region=region)
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_lpr_by_year(y):
    """
    按年份查找lpr
    :param y: 年 整型
    :return: Dataframe
    """
    queryset = LprPerMonth.objects.filter(year=y)
    df = pd.DataFrame(list(queryset.values()))
    return df


def find_lpr_by_month(y, m):
    """
    按照月份查找lpr
    :param y: 年 整型
    :param m: 月 整型
    :return: Dataframe
    """
    queryset = LprPerMonth.objects.filter(year=y, month=m)
    df = pd.DataFrame(list(queryset.values()))
    return df


def insert_result(stamp, y, error, p_value, a_value):
    """
    添加分析结果记录
    :param stamp: 时间戳 字符串
    :param y: 预测年份 整型
    :param error: 误差值 浮点型
    :param p_value: 预测值 浮点型
    :param a_value: 真实值 浮点型
    :return: Bool
    """
    result = AnalysisResult(timestamp=stamp, year=y, actual_value_field=a_value, predicted_value_field=p_value,
                            prediction_error=error)
    try:
        result.save()
        return True
    except Exception as e:
        print("录入异常：", e)
        return False


def update_result(stamp, y, error, p_value, a_value):
    """
    修改分析结果记录
    :param stamp: 时间戳 字符串
    :param y: 预测年份 整型
    :param error: 误差值 浮点型
    :param p_value: 预测值 浮点型
    :param a_value: 真实值 浮点型
    :return: Bool
    """
    try:
        result = AnalysisResult.objects.get(timestamp=stamp)
    except Exception as e:
        print("无此条记录，请检查时间戳")
        print(e)
        return False

    result.year = y
    result.prediction_error = error
    result.predicted_value_field = p_value
    result.actual_value_field = a_value

    try:
        result.save()
    except Exception as e:
        print("修改失败：", e)
        return False

    return True


def delete_result(stamp):
    """
    删除分析结果记录
    :param stamp: 时间戳
    :return: Bool
    """
    try:
        result = AnalysisResult.objects.get(timestamp=stamp)
    except Exception as e:
        print("无此条记录，请检查时间戳")
        print(e)
        return False

    try:
        result.delete()
    except Exception as e:
        print("删除失败：", e)
        return False

    return True


def insert_data(reg, y, gdp, loan, s_area, com_area, c_index, h_cost, invest, r_income, l_cost, population, lpr, h_price):
    """
    录入数据
    :param h_price: 房价
    :param reg: 地区 字符串
    :param y: 年份 整型
    :param gdp: 地区生产总值
    :param loan: 企业国内贷款
    :param s_area: 房屋销售面积
    :param com_area: 竣工房屋面积
    :param c_index: 居民消费价格指数
    :param h_cost: 房屋造价
    :param invest: 房地产开发投资额
    :param r_income: 居民可支配收入
    :param l_cost: 土地购置费用
    :param population: 城镇人口
    :param lpr: 贷款市场报价利率
    :return: Bool
    """
    data = Data(region=reg, year=y, gdp=gdp, company_loan=loan, sold_area=s_area, completed_area=com_area,
                consumption_index=c_index,
                house_cost=h_cost, investment=invest, residents_income=r_income, land_cost=l_cost,
                population=population, lpr=lpr, house_price=h_price)
    try:
        data.save()
        return True
    except Exception as e:
        print("录入异常：", e)
        return False


def delete_data(reg, y, gdp, loan, s_area, com_area, c_index, h_cost, invest, r_income, l_cost, population, lpr, h_price):
    """
    删除数据记录
    :param h_price: 房价
    :param reg: 地区 字符串
    :param y: 年份 整型
    :param gdp: 地区生产总值
    :param loan: 企业国内贷款
    :param s_area: 房屋销售面积
    :param com_area: 竣工房屋面积
    :param c_index: 居民消费价格指数
    :param h_cost: 房屋造价
    :param invest: 房地产开发投资额
    :param r_income: 居民可支配收入
    :param l_cost: 土地购置费用
    :param population: 城镇人口
    :param lpr: 贷款市场报价利率
    :return: Bool
    """
    data = Data(region=reg, year=y, gdp=gdp, company_loan=loan, sold_area=s_area, completed_area=com_area,
                consumption_index=c_index,
                house_cost=h_cost, investment=invest, residents_income=r_income, land_cost=l_cost,
                population=population, lpr=lpr, house_price=h_price)
    try:
        data.delete()
        return True
    except Exception as e:
        print("删除失败：", e)
        return False


def insert_monthly_lpr(y, m, lpr):
    """
    添加月度lpr
    :param y: 年份
    :param m: 月份
    :param lpr:
    :return: Bool
    """
    lpr_monthly = LprPerMonth(year=y, month=m, lpr=lpr)
    try:
        lpr_monthly.save()
        return True
    except Exception as e:
        print("录入异常：", e)
        return False


def delete_monthly_lpr(y, m, lpr):
    """
        删除月度lpr记录
        :param y: 年份
        :param m: 月份
        :param lpr:
        :return: Bool
        """
    lpr_monthly = LprPerMonth(year=y, month=m, lpr=lpr)
    try:
        lpr_monthly.delete()
        return True
    except Exception as e:
        print("删除失败：", e)
        return False
