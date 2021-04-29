from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 100)
    id = models.EmailField(primary_key=True)
    password = models.CharField(max_length = 100)

# 방법1 Member 에 OneToOneField 로 User 를 import 해서 넣어주기
# 방법2 Member 를 없애버리고, Account 가 User 를 외래키로 import 해서 받도록 한다.

class Account(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    accountNum = models.IntegerField(primary_key=True)
    totalNum = models.IntegerField()

class Payment(models.Model):
    accountNum = models.ForeignKey(Account, on_delete = models.CASCADE)
    count = models.IntegerField()
    payment = models.IntegerField()
    payment_time = models.DateTimeField()
