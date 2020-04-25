from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Physician(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
        #maximum numbers of shifts/month
    maxShiftLoad = models.IntegerField(default=5)
    phoneNumber = PhoneNumberField()

    SPECIALTY_CHOICES = (
        ('Family Medicine', 'Family Medicine'),
        ('Surgery', 'Surgery'),
        ('Hospice and Palliative Medicine', 'Hospice and Palliative Medicine'),
        ('Internal Medicine', 'Internal Medicine'),
        ('', '-----'),
    )

    specialty = models.CharField(
        max_length=50,
        choices=SPECIALTY_CHOICES,
        default='',
        blank=True,
    )

    def __str__(self):
        return self.lastName
