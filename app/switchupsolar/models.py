from django.db import models


class SendMessage(models.Model):
    msg = models.CharField(max_length=1000, null=False)
    num = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.msg}"
