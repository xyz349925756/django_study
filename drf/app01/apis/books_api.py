# from rest_framework.serializers import ModelSerializer
# from app01.models import Book,Student
#
#
# class BookModelSerializer(ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"
#
# class StudentSerializer(ModelSerializer):
#     class Meta: # 元
#         model = Student
#         fields = ["name","score"]  # 调整显示的字段


# def check_name(data):
#     if data.startswith('sb'):
#         raise ValueError('不能包含sb')
#     else:
#         return data
from app01.models import Student
from rest_framework import serializers

class StuSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=16,min_length=3,
                                 error_messages={
                                     'max_length':'最大值不能超过16位',
                                     'min_lenght':'最小不能低于3位',
                                     'required':'name 不能为空',
                                 })
    ab1 = serializers.IntegerField(source='age',error_messages={
        'required':'age 不能为空'
    })
    score = serializers.IntegerField(error_messages={
        'required':'score 不能为空'
    })

    # 局部
    # def validate_name(self, data):
    #     # 校验name
    #     # print(data,type(data)) # 薛子异 <class 'str'>
    #     """
    #       NotImplementedError: `update()` must be implemented.
    #       File "F:\Django_Project_Dir\drf\app01\views.py", line 40, in put
    #       stu_ser.save()
    #     """
    #     if len(data) > 3 and len(data) < 16:
    #         return data
    #     else:
    #         raise ValueError('name 不符合规范!')


    # 全局
    # def validate(self, data):
    #     print(data)
    #     age = data.get('age')
    #     score = data.get('score')
    #     if age == score:
    #         raise ValueError('age = score')
    #     else:
    #         return data




    # 定义一个update方法,不然views.py 中的stu_ser.save()提示没有update 为什么需要重写update呢?
    # 重写类的update方法. 子类重新定义了父类的方法,所以需要重写
    def update(self, instance, validated_data):
        """
        :param instance: 是Stu这个对象
        :param validated_data: 是 校验后的数据
        :return:
        """
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.score = validated_data.get('score')
        instance.save()
        return instance


    def create(self, validated_data):
        instance = Student.objects.create(**validated_data)
        return instance


class StuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['name','age'] # 指定需要序列化的字段
        # exclude=('name',) # 元组 tuple  #跟fields不能都写，写谁，就表示排除谁
        # read_only_fields = ('name',)
        extra_kwargs = {
            'name':{'write_only':True}
        }

from rest_framework.response import Response
import rest_framework.status