# django-celery
```
#centos6.7
#python2.7
#后台账号：root 密码：qq123456

yum install rabbitmq-server
/etc/init.d/rabbitmq-server start
pip install virtualenv

virtualenv ./env2.7
source env2.7/bin/activate
pip install -r mysite/pip_requirements.txt 

cd mysite
开启worker
python manage.py celery worker --loglevel=info

调用任务：
$ python manage.py shell
In [1]: from main.tasks import add
In [2]: a=add.delay(1,1)
In [3]: a.ready() #worker未开启
Out[3]: False
In [4]: a=add.delay(1,1) #开启worker，重新执行
In [5]: a.ready()
Out[5]: True
In [9]: a.get() #Waits until the task is done and returns the retval.
Out[9]: 2
In [10]: a.successful()
Out[10]: True
```
