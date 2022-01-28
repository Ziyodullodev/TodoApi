from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey( User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.date}"
    def newga_ozgartir(self):
        self.status = 'new'
        self.save()
    def finishga_ozgartir(self):
        self.status = 'finished'
        self.save()
