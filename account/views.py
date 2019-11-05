from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomerRegistrationForm


class CustomerRegistrationView(CreateView):
    """
    Registration view for new shop customer.
    Auto login registered customer.
    """
    template_name = 'register/register.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('shop:product_list')

    def form_valid(self, form):
        result = super(CustomerRegistrationView,
                       self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result
