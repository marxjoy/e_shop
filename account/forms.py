from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserAdress


class CustomerRegistrationForm(UserCreationForm):
    """
    Registration Form for new Customers. Provides data to
    create the User model and the UserAdress model.
    """
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    company_name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=50)
    street_number = forms.CharField(max_length=10)
    apartment_number = forms.CharField(max_length=10)
    zip_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email',
                  "password1", "password2", 'company_name', 'street',
                  'street_number', 'apartment_number', )

    def save(self, commit=True):
        user = super(CustomerRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        # create UserAdress Model
        adress = UserAdress(
                    user=user,
                    company_name=self.cleaned_data["company_name"],
                    name=user.first_name,
                    last_name=user.last_name,
                    street=self.cleaned_data["street"],
                    street_number=self.cleaned_data["street_number"],
                    apartment_number=self.cleaned_data["apartment_number"],
                    zip_code=self.cleaned_data["zip_code"],
                    city=self.cleaned_data["city"],
                        )
        adress.save()
        user.save()
        return user