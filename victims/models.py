from django.db import models
from django.utils import timezone
import datetime
from users.models import User

class Victim(models.Model):
    is_complete = models.IntegerField(choices=[(1, 'Complete'), (0, 'Not complete')], default=0)
    gender = models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], default=1)
    firstname = models.CharField(max_length=40, default='')
    lastname = models.CharField(max_length=40, default='')
    birthdate = models.DateField(default=datetime.date.today)
    address = models.TextField(max_length=200, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.lastname