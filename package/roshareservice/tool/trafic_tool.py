# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice的流量工具类，主要功能提供流量设置
"""
模块介绍
-------

这是一个roshareservice的流量工具类，主要功能提供流量设置

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）流量设置
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



import pandas as pd
from roshareservice.tool.info_tool import get_roshareservice_metadb_connection



####### roshareservice的流量工具类 ###########################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）无                                                                ###
### 主要功能：                                                             ###
### （1）流量设置                                                           ###
#############################################################################



###### roshareservice的流量工具类 #################################################################
#################################################################################################



### 获取用户流量
def get_user_trafic(user):
    '''
    函数功能：

        定义一个获取用户流量的函数

    参数：
        user (str): 用户名称
    
    返回：
        tmp_trafic (str): 用户对应的流量
    '''   

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 使用pandas读取数据，并判断是否已经存在该用户,存在则返回已登录，不存在则提示使用注册用户接口
    select_sql = "SELECT * FROM roshareserviceInfo"
    result_df = pd.read_sql(select_sql,con=roshareservice_metadb_connection)
    tmp_trafic = result_df[result_df['user'] == user]['trafic'].tolist()[0]

    return tmp_trafic



### 设置用户流量
def set_user_trafic(user,trafic_num):
    '''
    函数功能：

        定义一个设置用户流量的函数

    参数：
        user (str): 用户名称
        trafic_num (int): 流量数字
    
    返回：
        result (str): 返回结果信息
    '''

    ### 获取roshareservice元数据信息库连接
    roshareservice_metadb_connection = get_roshareservice_metadb_connection()
    ### 获取元数据信息库游标
    roshareservice_metadb_cursor = roshareservice_metadb_connection.cursor()
    ### 拼凑插入数据语句
    trafic_num = str(trafic_num)
    update_sql = "UPDATE roshareserviceInfo SET trafic = '{}' WHERE user = '{}'".format(trafic_num,user)
    print('User trafic update well done!====>>',update_sql)
    ### 执行插入数据语句
    roshareservice_metadb_cursor.execute(update_sql)
    ### 提交插入数据事务
    roshareservice_metadb_cursor.connection.commit()
    result = '{} trafic set well done!'.format(user)
    print(result)

    return result



###############################################################################################################
###############################################################################################################


