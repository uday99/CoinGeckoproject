from django.db import models

# Create your models here.

class UserModel(models.Model):
    username=models.CharField(primary_key=True,unique=True,max_length=150)
    password=models.CharField(max_length=150)
    confirmpass=models.CharField(max_length=150)
    def __str__(self):

        return self.username




class CryptoModel(models.Model):
    no=models.AutoField(primary_key=True)

    name=models.CharField(max_length=30,)
    image=models.CharField(max_length=100)
    symbol=models.CharField(max_length=10)
    price=models.FloatField()
    percent_change=models.FloatField()
    market_cap=models.IntegerField()
    market_cap_change_24h=models.IntegerField()

    user=models.ForeignKey(UserModel,on_delete=models.CASCADE)

    # def __str__(self):
    #
    #     return self.username