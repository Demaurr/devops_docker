from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    dsu_id = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return f"{self.name} ({self.dsu_id})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'