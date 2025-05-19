from django.db import models


class FormData(models.Model):
    dynamic_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Form №{self.id}"
