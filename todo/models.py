from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICE = [('PENDING', 'DENDOINF'), ('DONE', 'DONE')]


class Create(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, null=False, default='PENDING')

    def __str__(self):
        return self.task
