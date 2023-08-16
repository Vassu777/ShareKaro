from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)

    mobile_val = RegexValidator(
        regex = r'^\+?1?\d{9,15}$',
        message = 'Enter valid mobile number'
    )

    mobile_number = models.CharField(validators = [mobile_val],max_length=17)


