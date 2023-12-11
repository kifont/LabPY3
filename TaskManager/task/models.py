from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=255, default='')


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255, default='')
    Desc = models.TextField()
    Deadline = models.DateTimeField()
    Priority = models.IntegerField()
    Status = models.CharField(max_length=255, default='')
    Date = models.DateTimeField()
