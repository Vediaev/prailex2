from django.db import models
from django.contrib.auth.models import User


class HelpModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_user = models.CharField(max_length=50, blank=True, null=True)  # Клиент или Юрист
    type_of_profile = models.CharField(max_length=50, blank=True, null=True)  # Физическое лицо, юр. лицо, ИП ...
