# RoShareService

![shields_version](/static/shields_version.svg)    ![shields_license](/static/shields_license.svg)    ![shields_author](/static/shields_author.svg)    ![shiedls_python](/static/shields_python.svg)

![roshare_symbol](/static/roshare_symbol.jpeg)


## 介绍
+ RoShareService是一个数据服务包，主要功能是为底层数据向外提供了一个接口服务,可实现用户权限验证和流量限制。roShareService采用Client-Server架构设计，服务端使用HTTP协议构建数据服务的OpenAPI,暂时采用GET-method；用户权限采用token机制。


## 安装
roShareService采用Python开发，得益于Python良好的社区环境，安装支持Pythonic风格的各种管理器。

```bash
	$ pip install roshareservice-0.1.1-xxxxxxxxxxxx.whl
```


## 快速指南
### 服务端使用
+ 对于服务端数据服务启动，首先使用roShareService命令行进行元数据库初始化,然后再启动服务端服务。以下是roshareservicectl命令行示例：

```bash
	$ roshareservicectl set-metadb

	$ roshareservicectl start-service 
```


## 设计
+ 采用Client-Server架构设计
+ 服务端使用HTTP协议构建数据服务的OpenAPI
+ 用户权限采用token机制
+ 用户流量限制


### 技术列表
+ 微服务-FastAPI
+ 加密验证-Token-JWT技术
+ 数据库-SQLite3


### 设计UML图
以下是设计的UML图：
![roshareserviceuml](/static/RoShareServiceUML.png)