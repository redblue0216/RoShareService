# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice服务应用第三方数据接口路由类，主要使用fastapi搭建ASGI服务器
"""
模块介绍
-------

这是一个roshareservice服务应用第三方数据接口路由类，主要使用fastapi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）roshareservice服务应用第三方数据接口路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fastapi import APIRouter
from roshareservice.tool.info_tool import get_roshareservice_metadb_connection,encrypt_password
from roshareservice.tool.token_tool import encode_token,get_user_token,decode_token
from roshareservice.tool.trafic_tool import get_user_trafic,set_user_trafic
from roshareservice.tool.request_tool import collect_params,request_pretreate,get_tushare_data
# from roshareservice.service.dbconnection import db_engine
from roshareservice.service.cons import TUSHARE_BASEDATA_DICT,TUSHARE_FINANCE_DICT,TUSHARE_INDEX_DICT,TUSHARE_NEWS_DICT
import pandas as pd
import time
import json



####### roshareservice服务应用第三方数据接口路由 #################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）fastapi                                                           ###
### 主要功能：                                                              ###
### （1）roshareservice服务应用-第三方数据接口数据管理                          ###
#############################################################################



###### roshareservice服务应用第三方数据接口路由操作 #############################################################
############################################################################################################



### 创建fastapi应用实例-第三方数据接口路由
tushare_data_router = APIRouter()


### 获取第三方数据接口数据路由
### 获取tushare沪深股票--基础数据--股票列表
@tushare_data_router.get("/get_tushare_stock_basic")
async def get_tushare_stock_basic(token_key,token,tushare_token,exchange,list_status,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--基础数据的函数，主要提供tushare沪深股票的基础数据--股票列表

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        exchange (str): 交易所 SSE上交所 SZSE深交所 BSE北交所
        list_status (str): 上市状态 L上市 D退市 P暂停上市，默认是L
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'stock_basic'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(exchange=exchange,list_status=list_status,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json


   
### 获取tushare沪深股票--基础数据--上市公司基本信息
@tushare_data_router.get("/get_tushare_stock_company")
async def get_tushare_stock_company(token_key,token,tushare_token,exchange,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--基础数据的函数，主要提供tushare沪深股票的基础数据--上市公司基本信息

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        exchange (str): 交易所 SSE上交所 SZSE深交所 BSE北交所
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'stock_company'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(exchange=exchange,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--行情数据--日线数据
@tushare_data_router.get("/get_tushare_daily")
async def get_tushare_daily(token_key,token,tushare_token,ts_code,start_date,end_date):
    '''
    函数功能：

        定义一个获取tushare沪深股票--行情数据的函数，主要提供tushare沪深股票的行情数据--日线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'daily'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--行情数据--周线数据
@tushare_data_router.get("/get_tushare_weekly")
async def get_tushare_weekly(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--行情数据的函数，主要提供tushare沪深股票的行情数据--周线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'weekly'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--行情数据--月线数据
@tushare_data_router.get("/get_tushare_monthly")
async def get_tushare_monthly(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--行情数据的函数，主要提供tushare沪深股票的行情数据--月线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'monthly'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--行情数据--每日指标数据
@tushare_data_router.get("/get_tushare_daily_basic")
async def get_tushare_daily_basic(token_key,token,tushare_token,ts_code,trade_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--行情数据的函数，主要提供tushare沪深股票的行情数据--每日指标数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'daily_basic'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_BASEDATA_DICT[entity].format(ts_code=ts_code,trade_date=trade_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--利润表数据
@tushare_data_router.get("/get_tushare_income")
async def get_tushare_income(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--利润表数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'income'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--资产负债表数据
@tushare_data_router.get("/get_tushare_balancesheet")
async def get_tushare_balancesheet(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--资产负债表数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'balancesheet'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--现金流量表数据
@tushare_data_router.get("/get_tushare_cashflow")
async def get_tushare_cashflow(token_key,token,tushare_token,ts_code,start_date,end_date):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--现金流量表数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'cashflow'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--业绩预告数据
@tushare_data_router.get("/get_tushare_forecast")
async def get_tushare_forecast(token_key,token,tushare_token,ann_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--业绩预告数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ann_date (str): 公告日期 (二选一)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'forecast'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ann_date=ann_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--业绩快报数据
@tushare_data_router.get("/get_tushare_express")
async def get_tushare_express(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--业绩快报数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'express'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--财务数据--财务指标数据
@tushare_data_router.get("/get_tushare_fina_indicator")
async def get_tushare_fina_indicator(token_key,token,tushare_token,ts_code):
    '''
    函数功能：

        定义一个获取tushare沪深股票--财务数据的函数，主要提供tushare沪深股票的财务数据--财务指标数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 股票代码（支持多个股票同时提取，逗号分隔）

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'fina_indicator'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_FINANCE_DICT[entity].format(ts_code=ts_code)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--指数数据--日线数据
@tushare_data_router.get("/get_tushare_index_daily")
async def get_tushare_index_daily(token_key,token,tushare_token,ts_code,start_date,end_date):
    '''
    函数功能：

        定义一个获取tushare沪深股票--指数数据的函数，主要提供tushare沪深股票的指数数据--日线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 指数代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'index_daily'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_INDEX_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--指数数据--周线数据
@tushare_data_router.get("/get_tushare_index_weekly")
async def get_tushare_index_weekly(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--指数数据的函数，主要提供tushare沪深股票的指数数据--周线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 指数代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'index_weekly'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_INDEX_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--指数数据--月线数据
@tushare_data_router.get("/get_tushare_index_monthly")
async def get_tushare_index_monthly(token_key,token,tushare_token,ts_code,start_date,end_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--指数数据的函数，主要提供tushare沪深股票的指数数据--月线数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        ts_code (str): 指数代码（支持多个股票同时提取，逗号分隔）
        start_date (str): 开始日期(YYYYMMDD)
        end_date (str): 结束日期(YYYYMMDD)
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'index_monthly'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_INDEX_DICT[entity].format(ts_code=ts_code,start_date=start_date,end_date=end_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--指数数据--大盘每日指标数据
@tushare_data_router.get("/get_tushare_index_dailybasic")
async def get_tushare_index_dailybasic(token_key,token,tushare_token,trade_date,fields):
    '''
    函数功能：

        定义一个获取tushare沪深股票--指数数据的函数，主要提供tushare沪深股票的指数数据--大盘每日指标数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        trade_date (str): 交易日期 （格式：YYYYMMDD，比如20181018，下同）
        fields (str): 输出数据字段

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'index_dailybasic'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_INDEX_DICT[entity].format(trade_date=trade_date,fields=fields)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare沪深股票--指数数据--申万行业分类数据
@tushare_data_router.get("/get_tushare_index_classify")
async def get_tushare_index_classify(token_key,token,tushare_token,level,src):
    '''
    函数功能：

        定义一个获取tushare沪深股票--指数数据的函数，主要提供tushare沪深股票的指数数据--申万行业分类数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        level (str): 行业分级（L1/L2/L3）
        src (str): 指数来源（SW2014：申万2014年版本，SW2021：申万2021年版本）

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'index_classify'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_INDEX_DICT[entity].format(level=level,src=src)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



### 获取tushare另类数据--新闻快讯
@tushare_data_router.get("/get_tushare_news")
async def get_tushare_news(token_key,token,tushare_token,src,start_date,end_date):
    '''
    函数功能：

        定义一个获取tushare另类数据--新闻快讯的函数，主要提供tushare另类数据--新闻快讯数据

    参数：
        token_key (str): token密钥
        token (str): token串
        tushare_token (str): tushare的token信息
        src (str): 新闻来源
        start_date (datetime): 开始日期
        end_date (datetime): 结束日期

    返回：
        tmp_json (json): json结果字符串
    '''

    ### 获取接口字典中获取具体数据接口
    entity = 'news'#str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从roshareservice.service.cons中
    select_sql = TUSHARE_NEWS_DICT[entity].format(src=src,start_date=start_date,end_date=end_date)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_tushare_data(pretreatment=pretreatment,tushare_token=tushare_token,select_sql=select_sql)
    print('===========================================')
    print(tmp_json)

    return tmp_json



####################################################################################################################
####################################################################################################################


