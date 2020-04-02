from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30,verbose_name="客户端号")
    score = models.CharField(max_length=10,verbose_name="分数")

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'message'