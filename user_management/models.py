from django.db import models
from django.conf import settings
from django.utils import timezone

#Model for saving user details
class UserData(models.Model):
    user_id = models.CharField(max_length=50,unique=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    tz = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name_plural = "UserData"
    def __str__(self):
        return self.real_name
    
#Model for saving period activity of each user
class ActivityPeriod(models.Model):
    user = models.ForeignKey(UserData, blank=True, null=True, on_delete=models.CASCADE,related_name="activity_user")
    month = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    class Meta:
        verbose_name_plural = "ActivityPeriod"
    def __str__(self):
        return self.user.real_name