from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True
    )
    display_name = models.CharField(max_length=30)
    user_icon_url = models.URLField()
    user_bio = models.CharField(max_length = 100)
    user_dictionaly = models.CharField(max_length = 200)
    user_nn_index = models.IntegerField(null=True)
    def __str__(self):
        return self.display_name