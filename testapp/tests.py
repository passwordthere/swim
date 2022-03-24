import os

import django
from rest_framework import serializers
from django.test import TestCase

# Create your tests here.
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Swim.settings")

# 让django进行一次初始化
django.setup()


class User(object):
    """用户类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()


# 序列化基本使用
if __name__ == '__main__':
    # 用户对象
    user = User(name="Monkey", age=18)
    res = UserSerializer(user)
    dict = res.data
    print(dict)

# # 反序列化-基本使用-数据校验
# if __name__ == '__main__':
#     # 假如现在客户端给服务器传递了两个参数:那name,age,利用这两个数据创建一个用户的对象,但是需要先进行数据校验
#     req_data = {
#         "name": "Money",
#         "age": 24
#     }
#     # 反序列化-数据校验
#     serializer = UserSerializer(data=req_data)
#     res = serializer.is_valid()
#     print(res)
#
#     # 获取校验出错的信息
#     print(serializer.errors)
#
#     # 获取校验之后的数据
#     print(serializer.validated_data)
