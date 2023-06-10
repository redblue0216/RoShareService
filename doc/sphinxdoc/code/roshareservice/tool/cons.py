# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个元数据信息库参数管理脚本，主要用于存储相应参数
"""
模块介绍
-------

这是一个元数据信息库参数管理脚本，主要用于存储相应参数

    功能：             

        （1）元数据信息库参数管理

类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



import yaml
import roshareservice as rs



####### 元数据信息库参数管理 ########################################################
### 功能：                                                                     ###
### （1）元数据信息库参数管理                                                     ###
#################################################################################



####### 元数据信息库参数管理 ###############################################################################
########################################################################################################



### roshareservice_roshareservice_metadb_PATH：roshareservice数据库路径
### 从配置文件roshareservice_config.yaml中获取
# roshareservice_roshareservice_metadb_PATH = r'D:\Workspace\JiYuan\roshareservice\Demo\roshareservice.db'
roshareservice_package_path = rs.__file__.replace('__init__.py','')
roshareservice_config_file = open('{}roshareservice_config.yaml'.format(roshareservice_package_path),encoding='UTF-8')
roshareservice_config_yaml = yaml.load(roshareservice_config_file,Loader=yaml.FullLoader)
roshareservice_metadb_path = roshareservice_config_yaml['roshareservice_metadb_path']
roshareservice_METADB_PATH = r'{}'.format(roshareservice_metadb_path)



########################################################################################################
########################################################################################################


