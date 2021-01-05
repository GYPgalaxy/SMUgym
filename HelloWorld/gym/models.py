from django.db import models

# Create your models here.
class Gender(models.TextChoices):
    MAN = '男'
    WOMAN = '女'
    UNKOWN = '未知'


# 教练
class Coach(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=11, unique=True)
    gender = models.CharField(max_length=4,
                            choices=Gender.choices,
                            default=Gender.UNKOWN)
    birthday = models.DateField(auto_now=True)
    info = models.TextField(default='这里空荡荡的，什么也没有。')

    def __str__(self):
        return self.name


#用户
class User(models.Model):
    name = models.CharField(max_length=200, default='普通用户')
    tel = models.CharField(max_length=11, unique=True)
    gender = models.CharField(max_length=4,
                            choices=Gender.choices,
                            default=Gender.UNKOWN)
    birthday = models.DateField(auto_now=True)
    regtime = models.DateField(auto_now=True)
    isvip = models.BooleanField(default=False)
    vipstart = models.DateTimeField(auto_now=True)
    vipend = models.DateTimeField(auto_now=True)
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 课程
class Course(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    start = models.DateField()
    end = models.DateField()
    maxnum = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return self.name

#健康报告
class PhyTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coach= models.ForeignKey(Coach, on_delete=models.CASCADE)
    time = models.DateTimeField()
    height = models.FloatField()
    weight = models.FloatField()
    muscle = models.FloatField()
    fat = models.FloatField()
    water = models.FloatField()

#储物柜
class Locker(models.Model):
    location = models.CharField(max_length=200)
    isavailable = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.location

#课程订单
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    star = models.IntegerField()

#留言
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    msg = models.TextField()
