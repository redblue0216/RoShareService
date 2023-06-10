# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个信息工具类，主要功能创建元数据库，主要技术sqlite3
"""
模块介绍
-------

这是一个信息工具类，主要功能创建元数据信息库，主要技术sqlite3

    功能：             

        （1）元数据信息库创建

类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



from roshareservice.tool import cons as ct
import sqlite3
import hashlib
import roshareservice as rs



####### 信息工具类 ###############################################################
### 功能：                                                                    ###
### （1）元数据信息库创建                                                       ###
#################################################################################



####### 信息工具类 #######################################################################################
########################################################################################################



### 创建roshareservice元数据信息库
def create_roshareservice_metadb(roshareservice_metadb_path = ct.roshareservice_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个创建roshareservice元数据信息库的函数

    参数：
        roshareservice_metadb_path (str): roshareservice元数据信息库路径

    返回：
        result (str): 创建成功结果信息
    '''

    ### 获取包安装后的路径site-packages/roshareservice/
    roshareservice_metadb_path_in_pkg = rs.__file__.replace('__init__.py','') 
    ### 开始创建数据库
    roshareservice_metadb_connection = sqlite3.connect(roshareservice_metadb_path_in_pkg + roshareservice_metadb_path)
    roshareservice_metadb_cursor = roshareservice_metadb_connection.cursor()
    roshareservice_metadb_cursor.execute('''CREATE TABLE IF NOT EXISTS roshareserviceInfo(
        user TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL,
        trafic TEXT NOT NULL 
    )
    ''')
    roshareservice_metadb_cursor.close()
    roshareservice_metadb_connection.close()
    result = 'roshareservice metadb create well done!====>>{}'.format(roshareservice_metadb_path)
    print(result)

    return result



### 获取roshareservice元数据信息库操作游标
def get_roshareservice_metadb_connection(roshareservice_metadb_path = ct.roshareservice_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个获取roshareservice元数据信息库操作游标的函数

    参数：
        roshareservice_metadb_path (str): roshareservice元数据信息库路径

    返回：
        roshareservice_metadb_connection (obj): roshareservice元数据信息库连接
    '''

    
    ### 获取包安装后的路径site-packages/roshareservice/
    roshareservice_metadb_path_in_pkg = rs.__file__.replace('__init__.py','')   
    ### 开始创建数据库  
    roshareservice_metadb_connection = sqlite3.connect(roshareservice_metadb_path_in_pkg + roshareservice_metadb_path)

    return roshareservice_metadb_connection



### 加密密码
def encrypt_password(password,salt='roshareservice',algorithm='md5'):
    '''
    函数功能：

        定义一个加密密码的函数，默认使用md5加密算法

    参数：
        password (str): 密码
        salt (str): 密码加盐，默认为roshareservice
        algorithm (str): 加密算法

    返回：
        encrypted_pwd (str): 加密后的密码
    '''

    SALT = salt
    md5_salt = hashlib.md5((password + SALT).encode('utf-8'))
    encrypted_pwd = md5_salt.hexdigest()

    return encrypted_pwd



#############################################################################################################
#############################################################################################################


