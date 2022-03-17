from django.db import models

# Create your models here.
from django.contrib.auth.models import User,AbstractUser,BaseUserManager

class User(AbstractUser):
    options=(("employer","employer"),
             ("candidate","candidate")
             )

    role=models.CharField(max_length=120,choices=options,default="candidate")

