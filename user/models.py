from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    tg_id = models.fields.PositiveBigIntegerField(null=True)
    tg_username = models.fields.CharField(max_length=255, null=True)
    is_premium = models.fields.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    REQUIRED_FIELDS = ["first_name"]
