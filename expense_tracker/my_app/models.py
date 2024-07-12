from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    @classmethod
    def cat_dict(cls):
        all_objects = Category.objects.all()
        return list(map(lambda obj: (obj.name,obj.name), all_objects))

class Book(models.Model):

    id_num = models.CharField(max_length=64)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    publish_date = models.DateField()
    category = models.ForeignKey(Category,  blank=True, null=True, on_delete= models.SET_NULL)
    distribution_expense = models.FloatField()

    def __str__(self):
        return (f'id_num: {self.id_num}, title: {self.title}, author: {self.author}, publish_date: {self.publish_date}category: {self.category}, distribution_expense: {self.distribution_expense}')


