# 项目操作手册

## **项目结构**

<pre> 
/myblog
|-- /client                    # 前端应用
|   |-- /public                # 存放公共文件
|   |-- /src                   # 源代码目录
|   |   |-- /assets            # 静态资源
|   |   |-- /components        # 可复用的组件
|   |   |-- /router            # 前端路由配置
|   |   |-- /views             # 页面组件
|   |   |-- App.vue            # 主应用组件
|   |   |-- main.js            # 入口文件
|   |-- /node_modules          # 运行环境依赖（忽略）
|-- /server                    # 后端应用
|   |-- /api                   # API相关代码
|   |   |-- config.py          # 配置文件
|   |   |-- models/            # 数据模型
|   |   |-- resources/         # API资源模块
|   |   |-- utils.py           # 工具函数
|   |   |-- app.py             # 初始化文件
|   |-- /venv/                 # 虚拟环境（忽略）
|   |-- requirements.txt       # 项目依赖
|   |-- run.py                 # 应用启动文件
|-- .gitignore                 # Git忽略文件配置
|-- README.md                  # 项目说明文档

</pre>

## 操作步骤

### 环境配置

#### 配置前端环境

1. 安装 node.js 和 npm

   - 下载并安装 [Node.js](https://nodejs.org/)
   - Node.js 安装包通常会包含 npm（Node 包管理器）

2. 安装 Vue CLI

   在命令行中运行以下命令安装 Vue CLI：

   ```
   npm install -g @vue/cli
   ```

3. 创建 Vue3 项目
   ```
   vue create client
   项目依赖有typescript、router
   ```
4. 安装相应的包
   ```
   cd client
   npm install axios
   npm install element-plus
   ```

#### 配置后端环境

1. 安装 Python（此项目是 python3.8）

   - 下载并安装 [Python](https://www.python.org/)

   - 安装 virtualenv

     ```
     pip install virtualenv
     ```

   - 若是不用 virtualenv，也可以安装 anaconda3 来进行虚拟环境的创建

2. 虚拟环境

   - 创建虚拟环境

     ```
     cd .\server
     virtualenv venv
     virtualenv -p "你的python路径\python.exe" venv
     ```

   - 激活虚拟环境

     ```
     cd .\server\venv\Scripts
     .\activate
     ```

   - 安装环境依赖

     ```
     cd .\server
     pip install -r requirements.txt
     ```

3. 安装redis
   
   - 可以参考[redis安装教程](https://blog.csdn.net/weixin_65777087/article/details/131462691?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171145697216800227493776%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171145697216800227493776&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-131462691-null-null.142^v100^pc_search_result_base5&utm_term=redis%E5%AE%89%E8%A3%85&spm=1018.2226.3001.4187)
   - 可以从官网下载[redis](https://redis.io/download)

#### 配置数据库

1. 安装并配置[MySQL](https://www.mysql.com/cn/)数据库

2. 在 `.\server\api\config.py` 配置配置文件中数据库连接参数。

3. 初始化数据库

   ```
   打开server文件夹
   python manage.py init_db
   ```

#### 运行前后端应用

1. 运行前端

   ```
   打开client文件夹
   npm run serve
   ```

2. 运行后端

   ```
   打开server文件夹
   python run.py
   ```

## **学习资料**

- Flask 官方文档： [Flask](https://www.osgeo.cn/flask/)
- Flask-SQLAlchemy 官方文档： [SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/)
- Flask-Migrate 官方文档： [Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- Vue 官方文档：[Vue](https://cn.vuejs.org/)
- Element-Plus 官方文档：[Element-Plus](https://element-plus.org/zh-CN/)
- Redis 官方文档 [Redis](https://redis.io/)


## **版本**
v1.0.0 实现了大杂烩系统的打卡和打卡统计功能。