# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice的token工具类，主要功能提供token验证和从token中获取基本信息，主要技术JWT
"""
模块介绍
-------

这是一个roshareservice的token工具类，主要功能提供token验证和从token中获取基本信息，主要技术JWT

设计模式：

    无

关键点：    

    （1）JWT

主要功能：            

    （1）token验证与信息获取
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



import pandas as pd
import jwt 
from roshareservice.tool.info_tool import get_roshareservice_metadb_connection



####### roshareservice的token工具类 ##########################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）JWT                                                              ###
### 主要功能：                                                             ###
### （1）token验证与信息获取                                                ###
############################################################################



###### roshareservice的token工具操作 #################################################################
####################################################################################################



### 编码token
def encode_token(payload,key,algorithms = "HS256"):
    '''
    函数功能：

        定义一个编码token的函数，主要功能编码目标token,主要技术JWT

    参数：
        payload (dict): 待编码数据字典
        key (str): 关键密钥
        algorithms (str): 加密算法，默认为HS256

    返回：
        encoded_jwt (str): 已编码数据字符串
    '''

    encoded_jwt = jwt.encode(payload=payload,key=key,algorithm=algorithms)
    
    return encoded_jwt



### 解码token
def decode_token(encoded_token,key,algorithms = "HS256"):
    '''
    函数功能：

        定义一个解码token的函数，主要功能解码目标token,主要技术JWT

    参数：
        encoded_token (str): 已编码token
        key (str): 关键密钥
        algorithms (str): 加密算法，默认为HS256

    返回：
        decoded_jwt (dict): 解码的数据字典
    '''

    decoded_jwt = jwt.decode(jwt=encoded_token,key=key,algorithms=algorithms)
    
    return decoded_jwt



### 获得用户token
def get_user_token(user):
    '''
    函数功能：

        定义一个获取用户token的函数

    参数：
        user (str): 用户名称
    
    返回：
        tmp_token (str): 用户对应的token
    '''

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 使用pandas读取数据，并判断是否已经存在该用户,存在则返回已登录，不存在则提示使用注册用户接口
    select_sql = "SELECT * FROM roshareserviceInfo"
    result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
    tmp_token = result_df[result_df['user'] == user]['token'].tolist()[0]

    return tmp_token



############################################################################################################
############################################################################################################


