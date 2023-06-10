# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareservice服务应用主路由类，主要使用fastapi搭建ASGI服务器
"""
模块介绍
-------

这是一个roshareservice服务应用主路由类，主要使用fastapi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）roshareservice服务应用主路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fastapi import FastAPI
import uvicorn
# import sys
# sys.path.append('/home/shihua/tulip/workspace/roshareservice/demo/') ### 打包后需要注释掉
# print(sys.path)
from roshareservice.service.user_router import user_router
from roshareservice.service.tushare_router import tushare_data_router 



####### roshareservice服务应用主路由 ###########################################
### 设计模式：                                                              ###
###     无                                                                 ###
### 关键点：                                                                ###
### （1）fastapi                                                           ###
### 主要功能：                                                              ###
### （1）roshareservice服务应用                                             ###
#############################################################################



###### roshareservice服务应用主路由操作 ###############################################################
####################################################################################################



### 创建fastapi应用实例
app = FastAPI()
app.include_router(user_router,prefix="/user",tags=['user'])
app.include_router(tushare_data_router ,prefix="/tushare",tags=['tushare'])



if __name__ == '__main__':
    uvicorn.run(app='main_router:app',host='0.0.0.0',port=11911,reload=True) ### app参数需要使用字符串格式的时候，才可以添加reload和debug参数，debug参数在新版uvicorn中不加入。



####################################################################################################
####################################################################################################


