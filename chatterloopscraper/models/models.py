from django.db import models

class Chatterloopusers(models.Model):
    userID = models.CharField(max_length=550)
    isActivated = models.BooleanField()
    isVerified = models.BooleanField()

    def __str__(self):
        return self.userID