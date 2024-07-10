from django.db import models

# Create your models here.
class Book(models.Model):

    id_num = models.IntegerField()
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publish_date = models.DateField()
    category = models.CharField(max_length=32)
    distribution_expense = models.FloatField()
    def __str__(self):
        return (f'id_num: {self.id_num}, title: {self.title}, author: {self.author}, publish_date: {self.publish_date}category: {self.category}, distribution_expense: {self.distribution_expense}')
class Category(models.Model):
    category = models.CharField(max_length=64)