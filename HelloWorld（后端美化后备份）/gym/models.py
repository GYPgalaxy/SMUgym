from django.db import models

# Create your models here.
class Gender(models.TextChoices):
    MAN = '男'
    WOMAN = '女'
    UNKOWN = '未知'


# 教练
class Coach(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=11)
    gender = models.CharField(max_length=4,
                            choices=Gender.choices,
                            default=Gender.UNKOWN)
    birthday = models.DateField()
    info = models.TextField()

    def __str__(self):
        return self.name


#用户
class User(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=11)
    gender = models.CharField(max_length=4,
                            choices=Gender.choices,
                            default=Gender.UNKOWN)
    birthday = models.DateField()
    regtime = models.DateField()
    isvip = models.BooleanField()
    vipstart = models.DateTimeField()
    vipend = models.DateTimeField()

    def __str__(self):
        return self.name


# 课程
class Course(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    start = models.DateField()
    end = models.DateField()
    maxnum = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return self.course_name

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
    isavailable = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.location