from django.db import models


# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.CharField(max_length=10)
    is_paid = models.CharField(max_length=50)
    # will_be_paid = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    comments = models.TextField(default=None)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'
