from django.db import models


# Create your models here.

class User(models.Model):
    account = models.CharField(verbose_name="账号", max_length=64)
    password = models.CharField(verbose_name="密码", max_length=64)
    name = models.CharField(verbose_name="姓名", max_length=64)
    avatar = models.CharField(verbose_name="头像地址", max_length=255)
    token = models.CharField(verbose_name="token", max_length=255)

    last_login_time = models.DateTimeField(verbose_name="上次登录时间", auto_now=True)
