from django.db import models
from django_extensions.db.models import TimeStampedModel
from accounts.models import VokoUser


class EventLog(TimeStampedModel):
    class Meta:
        app_label = "log"

    id = models.AutoField(primary_key=True)
    operator = models.ForeignKey(VokoUser,
                                 related_name="operator_logs",
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    user = models.ForeignKey(VokoUser, null=True, blank=True,
                             related_name="user_logs",
                             on_delete=models.SET_NULL)
    event = models.CharField(max_length=255)
    extra = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event
