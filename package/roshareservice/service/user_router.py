# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice服务应用用户路由类，主要使用fastapi搭建ASGI服务器
"""
模块介绍
-------

这是一个roshareservice服务应用用户路由类，主要使用fastapi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）roshareservice服务应用用户路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



from fastapi import APIRouter
from roshareservice.tool.info_tool import get_roshareservice_metadb_connection,encrypt_password
from roshareservice.tool.token_tool import encode_token
from roshareservice.tool.trafic_tool import get_user_trafic,set_user_trafic
import pandas as pd
import time
import json



####### roshareservice服务应用用户路由 ########################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）fastapi                                                          ###
### 主要功能：                                                             ###
### （1）Droshareservice服务应用-用户信息管理                                ###
############################################################################



###### roshareservice服务应用主路由操作 ###############################################################
####################################################################################################



### 创建fastapi应用实例-用户路由
user_router = APIRouter()



### 注册用户路由
@user_router.get("/register")
async def register(user,password):
    '''
    函数功能：

        定义一个注册用户的路由函数，主要功能提供注册功能

    参数：
        user (str): 用户名称
        password (str): 用户密码

    返回：
        info (dict): 路由动作反馈信息
    '''

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 使用pandas读取数据，并判断是否已经存在该用户,存在跳过，不存在则添加信息
    select_sql = "SELECT * FROM roshareserviceInfo"
    result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
    users_list = result_df['user'].tolist()
    if str(user) in set(users_list):
        result = 'User already exists!'
    else:
        ### 获取元数据信息库游标
        roshareservice_metadb_cursor = roshareservice_metadb_connection.cursor()
        ### 收集入库参数数据，一定转为str类型 ### 特别注意 ###
        user = str(user)
        password = str(encrypt_password(password=password)) ### 密码加密
        token = 'no_token'
        trafic = 'no_trafic'
        ### 拼凑插入数据语句
        inser_sql = "INSERT INTO roshareserviceInfo (user,password,token,trafic) VALUES ('{}','{}','{}','{}')".format(user,password,token,trafic)
        print('User info register well done!====>>',inser_sql)
        ### 执行插入数据语句
        roshareservice_metadb_cursor.execute(inser_sql)
        ### 提交插入数据事务
        roshareservice_metadb_cursor.connection.commit()
        result = 'User info register well done!'

    return {'info':result}



### 登录用户路由
@user_router.get("/login")
async def login(user,password):
    '''
    函数功能：

        定义一个登录用户的路由函数，主要功能提供登录功能

    参数：
        user (str): 用户名称
        password (str): 用户密码

    返回：
        info (dict): 路由动作反馈信息
    '''

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 使用pandas读取数据，并判断是否已经存在该用户,存在则返回已登录，不存在则提示使用注册用户接口
    select_sql = "SELECT * FROM roshareserviceInfo"
    result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
    users_list = result_df['user'].tolist()
    if str(user) in set(users_list):
        ### 加入密码验证步骤,通过则返回登录成功信息，失败则返回登录失败信息
        tmp_password = result_df[result_df['user'] == str(user)]['password'].tolist()[0]
        password = str(encrypt_password(password=password)) ### 密码加密
        if str(password) == str(tmp_password):
            result = 'User log in well done!'
        else:
            result = 'User password error!'
    else:
        result = 'Please register user!'

    return {'info':result}



### 获取对应用户名的token,包括重新生成token和返回生成的token
### 生成新的token
@user_router.get("/gen_token")
async def gen_token(user,token_key='password',effectivetime=6000):
    '''
    函数功能：

        定义一个生成token的路由函数，主要功能提供生成token功能

    参数：
        user (str): 用户名称
        token_key (str): token密钥
        effectivetime (int): token有效时间，以秒为单位，默认100分钟

    返回：
        info (dict): 路由动作反馈信息
    '''

    ### 加密密钥,这个很重要千万不能泄露了,此处默认使用用户自己注册时的密码
    token_key = str(token_key)
    if token_key == 'password':
        ### 获取roshareservice元数据信息库连接
        roshareservice_metadb_connection = get_roshareservice_metadb_connection()
        ### 使用pandas读取数据，并判断是否已经存在该用户,存在则返回已登录，不存在则提示使用注册用户接口
        select_sql = "SELECT * FROM roshareserviceInfo"
        result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
        ### 获取用户密码
        tmp_password = result_df[result_df['user'] == str(user)]['password'].tolist()[0]
        password = str(tmp_password)
        SECRET_KEY = str(password) 
    else:
        SECRET_KEY = str(token_key)   
    ### 设置过期时间,现在时间 + 有效时间(以秒为单位),示例100分钟 60 * 100 = 6000
    expire = time.time() + int(effectivetime)
    ### exp是固定写法必须得传,user为用户id,是自己存的值,不能存密码等敏感信息
    to_encode = {"exp":expire,"user":str(user)}
    ### 使用JWT生成token 
    encoded_jwt = encode_token(payload=to_encode,key=SECRET_KEY,algorithms='HS256')
    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 获取元数据信息库游标
    roshareservice_metadb_cursor = roshareservice_metadb_connection.cursor()
    ### 拼凑插入数据语句
    update_sql = "UPDATE roshareserviceInfo SET token = '{}' WHERE user = '{}'".format(encoded_jwt,user)
    print('User token update well done!====>>',update_sql)
    ### 执行插入数据语句
    roshareservice_metadb_cursor.execute(update_sql)
    ### 提交插入数据事务
    roshareservice_metadb_cursor.connection.commit()
    result = '{} jwt token generate well done!'.format(user)
    print(result)

    return {'info':result}



### 获取对应用户名的token,包括重新生成token和返回生成的token
### 从数据库中获取对应用户名的token
@user_router.get("/get_token")
async def get_token(user,password):
    '''
    函数功能：

        定义一个获取token的路由函数，主要功能提供获取token功能

    参数：
        user (str): 用户名称
        password (str): 用户密码

    返回：
        info (dict): 路由动作反馈信息
    '''

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 使用pandas读取数据，并判断是否已经存在该用户,存在则返回已登录，不存在则提示使用注册用户接口
    select_sql = "SELECT * FROM roshareserviceInfo"
    result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
    users_list = result_df['user'].tolist()
    if str(user) in set(users_list):
        ### 加入密码验证步骤,通过则返回登录成功信息，失败则返回登录失败信息
        tmp_password = result_df[result_df['user'] == str(user)]['password'].tolist()[0]
        password = str(encrypt_password(password=password)) ### 密码加密
        if str(password) == str(tmp_password):
            result = 'Get user {} token well done'.format(user)
            tmp_token = result_df[result_df['user'] == str(user)]['token'].tolist()[0]
        else:
            result = 'User password error!'
            tmp_token = 'no_token'
    else:
        result = 'Please register user!'
        tmp_token = 'no_token'
    print(result)

    return {'token':tmp_token}



### 获取用户流量数据
@user_router.get("/get_trafic")
async def get_trafic(user):
    '''
    函数功能：

        定义一个获取流量的路由函数，主要功能提供获取流量功能

    参数：
        user (str): 用户名称

    返回：
        trafic (dict): 用户剩余流量
    '''

    ### 开始执行获取流量函数
    tmp_trafic = get_user_trafic(user=user)

    return {'trafic':tmp_trafic}



### 设置用户流量数据
@user_router.get("/set_trafic")
async def set_trafic(user,trafic_num):
    '''
    函数功能：

        定义一个设置流量的路由函数，主要功能提供设置流量功能

    参数：
        user (str): 用户名称
        trafic_num (int): 流量数目

    返回：
        info (dict): 路由动作反馈信息
    '''

    ### 开始执行设置流量函数
    tmp_result = set_user_trafic(user=user,trafic_num=trafic_num)

    return {'info':tmp_result}



####################################################################################################
####################################################################################################


