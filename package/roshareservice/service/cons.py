# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个服务端参数管理脚本，主要用于存储相应参数、SQL查询语句和第三方数据接口
"""
模块介绍
-------

这是一个服务端参数管理脚本，主要用于存储相应参数、SQL查询语句和第三方数据接口

    功能：             

        （1）服务端参数管理、SQL查询语句和第三方数据接口管理

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################






####### 服务端参数管理 ############################################################
### 功能：                                                                     ###
### （1）服务端参数管理、SQL查询语句和第三方数据接口                                 ###
#################################################################################



####### 服务端参数管理 ####################################################################################
########################################################################################################



# ### dialect：数据库类型
# SERVICE_DIALECT = 'mysql'
# ### driver：数据库驱动选择
# SERVICE_DRIVER = 'pymysql'
# ### username：数据库用户名
# SERVICE_USERNAME = 'root'
# ### password： 用户密码
# SERVICE_PASSWORD = 'Passw0rd!'
# ### host：服务器地址
# SERVICE_HOST = '39.104.77.195'
# ### port：端口
# SERVICE_PORT = '3306'
# ### database：数据库
# SERVICE_DATABASE = 'stations_xjjx'



####### 第三方数据接口整理 ###################################################################################
###########################################################################################################



### tushare对应python查询接口
### tushare沪深股票--基础数据--股票列表
stock_basic = "stock_basic(exchange='{exchange}',list_status='{list_status}',fields='{fields}')"
### tushare沪深股票--基础数据--上市公司基本信息
stock_company = "stock_company(exchange='{exchange}',fields='{fields}')"
### tushare沪深股票--行情数据--日线数据
daily = "daily(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}')"
### tushare沪深股票--行情数据--周线数据
weekly = "weekly(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--行情数据--月线数据
monthly = "monthly(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--行情数据--每日指标数据
daily_basic = "daily_basic(ts_code='{ts_code}',trade_date='{trade_date}',fields='{fields}')"
### tushare沪深股票--财务数据--利润表数据
income = "income(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--财务数据--资产负债表数据
balancesheet = "balancesheet(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--财务数据--现金流量表数据
cashflow = "cashflow(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}')"
### tushare沪深股票--财务数据--业绩预告
forecast = "forecast(ann_date='{ann_date}',fields='{fields}')"
### tushare沪深股票--财务数据--业绩快报
express = "express(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--财务数据--财务指标数据
fina_indicator = "fina_indicator(ts_code='{ts_code}')"
### tushare沪深股票--指数数据--日线数据
index_daily = "index_daily(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}')"
### tushare沪深股票--指数数据--周线数据
index_weekly = "index_weekly(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--指数数据--月线数据
index_monthly = "index_monthly(ts_code='{ts_code}',start_date='{start_date}',end_date='{end_date}',fields='{fields}')"
### tushare沪深股票--指数数据--大盘每日指标数据
index_dailybasic = "index_dailybasic(trade_date='{trade_date}',fields='{fields}')"
### tushare沪深股票--指数数据--申万行业分类数据
index_classify = "index_classify(level='{level}',src='{src}')"
### tushare另类数据--新闻快讯
news = "news(src='{src}',start_date='{start_date}',end_date='{end_date}')"



####### 数据查询语句整理字典 #################################################################################################################
############################################################################################################################################



### 将具体业务场景数据查询汇集到一个字典中方便数据服务路由调用，避免写多个条件判断
### TuShare沪深股票--基础数据
TUSHARE_BASEDATA_DICT = {}
TUSHARE_BASEDATA_DICT['stock_basic'] = stock_basic
TUSHARE_BASEDATA_DICT['stock_company'] = stock_company
TUSHARE_BASEDATA_DICT['daily'] = daily
TUSHARE_BASEDATA_DICT['weekly'] = weekly
TUSHARE_BASEDATA_DICT['monthly'] = monthly
TUSHARE_BASEDATA_DICT['daily_basic'] = daily_basic
### TuShare沪深股票--财务数据
TUSHARE_FINANCE_DICT = {}
TUSHARE_FINANCE_DICT['income'] = income
TUSHARE_FINANCE_DICT['balancesheet'] = balancesheet
TUSHARE_FINANCE_DICT['cashflow'] = cashflow
TUSHARE_FINANCE_DICT['forecast'] = forecast
TUSHARE_FINANCE_DICT['express'] = express
TUSHARE_FINANCE_DICT['fina_indicator'] = fina_indicator
### TuShare沪深股票--指数数据
TUSHARE_INDEX_DICT = {}
TUSHARE_INDEX_DICT['index_daily'] = index_daily
TUSHARE_INDEX_DICT['index_weekly'] = index_weekly
TUSHARE_INDEX_DICT['index_monthly'] = index_monthly
TUSHARE_INDEX_DICT['index_dailybasic'] = index_dailybasic
TUSHARE_INDEX_DICT['index_classify'] = index_classify
### TuShare另类数据--新闻数据
TUSHARE_NEWS_DICT = {}
TUSHARE_NEWS_DICT['news'] = news



############################################################################################################################################
############################################################################################################################################


