from django.db import models


class Entry(models.Model):
    """An entry stores the user todo for the day

    Args:
        models (_type_): _description_
    """

    class Meta:
        verbose_name_plural = "entries"

    body = models.TextField()
    when = models.DateField()
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="entries",
    )
