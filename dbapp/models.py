from django.db import models
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.TextField(max_length=20)
    pcost=models.DecimalField(max_digits=10,decimal_places=4)
    pmdt=models.DateField()
    pexpdt=models.DateField()