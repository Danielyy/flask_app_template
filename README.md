功能说明
====
1. 基于flask的web页面。
2. 提供数据库支持。运行环境在config.py中配置
3. 提供email的账户注册，运行环境在config.py中配置
4. 提供角色权限控制


数据迁移
```angular2html
python3 manage.py db init #初始化
python3 manage.py db migrate -m "initial migration" #建立数据库迁移脚本
python3 manage.py db upgrade #升级初始化数据库
```
生成需求环境安装文件列表
```angular2html
pip freeze > requirements.txt
pip install -r requirements.txt
```
缺少MySQL_config文件的处理方式
```angular2html
apt-get install libmysqlclient-dev
```

配置邮箱
```angular2html
(venv) $ export MAIL_USERNAME=<mail username>
(venv) $ export MAIL_PASSWORD=<mail password>
在配置文件中修改SMTP服务器地址和端口
```


