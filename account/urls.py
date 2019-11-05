from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.CustomerRegistrationView.as_view(),
         name="register"),
]