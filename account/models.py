from django.conf import settings
from django.db import models


class UserAdress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='adress')
    company_name =  models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"""{self.name} {self.last_name}
               {self.company_name} 
               {self.street} {self.street_number} {self.apartment_number}
               {self.zip_code} {self.city}"""