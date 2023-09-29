
# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

# myapp/models.py
#from django.contrib.auth.models import AbstractUser

#class CustomUser(AbstractUser):
    # Add custom fields if needed
  #  pass
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title