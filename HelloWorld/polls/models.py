import datetime

from django.db import models
from django.utils import timezone

###
# 在这个投票应用中，需要创建两个模型：问题 Question 和选项 Choice。
# Question 模型包括问题描述和发布时间。Choice 模型有两个字段，
# 选项描述和当前得票数。每个选项属于一个问题。

# 每个模型被表示为 django.db.models.Model 类的子类。
# 每个模型有许多类变量，它们都表示模型里的一个数据库字段。

# 每个字段都是 Field 类的实例 - 比如，字符字段被表示为 CharField ，
# 日期时间字段被表示为 DateTimeField 。
# 这将告诉 Django 每个字段要处理的数据类型。

# 每个 Field 类实例变量的名字（例如 question_text 或 pub_date ）也是字段名，
# 所以最好使用对机器友好的格式。你将会在 Python 代码里使用它们，
# 而数据库会将它们作为列名。

# 定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。
# 这个参数的用处不止于用来定义数据库结构，也用于验证数据，
# 我们稍后将会看到这方面的内容。

# Field 也能够接收多个可选参数；在上面的例子中：
# 我们将 votes 的 default 也就是默认值，设为0。

# 注意在最后，我们使用 ForeignKey 定义了一个关系。
# 这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。
# Django 支持所有常用的数据库关系：多对一、多对多和一对一。
###

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text