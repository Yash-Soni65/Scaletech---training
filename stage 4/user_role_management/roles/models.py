from django.db import models



class Role(models.Model):
    """
    Represents a user role and the modules accessible to that role.
    """
    roleName = models.CharField(max_length=100, unique=True)
    accessModules = models.JSONField(default=list)
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.roleName

# Create your models here.
