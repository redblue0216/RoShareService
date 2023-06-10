# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice常用命令行接口类
"""
模块介绍
-------

这是一个roshareservice常用命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）roshareservice程序管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################



import click
import os
import sys
from rich.console import Console
from roshareservice.tool.info_tool import create_roshareservice_metadb
import roshareservice as ss



####### CLI命令行接口 ########################################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）click                                                            ###
### 主要功能：                                                             ###
### （1）roshareservice程序管理                                            ###
############################################################################



###### CLI命令行接口 ######################################################################
#########################################################################################



### roshareservice命令组
@click.group()
@click.help_option('-H','--help')
@click.version_option('-V','--version')
def roshareservice():
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======            Hello! Welcome to roshareservice                ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="red")


### roshareservice设置环境变量
@click.command(help="set up a meta database for roshareservice")
def set_metadb():
    console = Console()
    result = create_roshareservice_metadb()
    print(result)
    console.print('=================================================================>>>>>> roshareservice set a meta database',style="red")


### roshareservice启动后台服务
@click.command(help="start atom service")
def start_service():
    console = Console()
    print(ss.__file__)
    api_path = ss.__file__.replace('__init__.py','')### __init__.py前的roshareservice\需要去掉，打包后
    print(api_path)
    console.print('=================================================================>>>>>> roshareservice servive start',style="red")
    system_platform = sys.platform
    if system_platform == 'win32':
        os.system("{} & cd {} & python .\service\main_router.py".format(api_path[:2],api_path))
    elif system_platform == 'linux':
        # os.system("cd {} & python ./service/main_router.py".format(api_path))
        os.system("python {}service/main_router.py".format(api_path))
    # uvicorn api:app --reload --host '0.0.0.0' --port 11911


### 向roshareservice命令组添加命令
roshareservice.add_command(set_metadb) 
roshareservice.add_command(start_service)  


### python脚本主程化
if __name__ == '__main__':
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======            Hello! Welcome to roshareservice                ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="red")
    roshareservice()



#################################################################################################################################################
#################################################################################################################################################


