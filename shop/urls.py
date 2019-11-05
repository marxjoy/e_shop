from django.contrib import admin
from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductList.as_view(), name='product_list'),
    path('<int:id>/<slug:slug>/', views.ProductDetail.as_view(),
         name='product_detail'),
    path('search/', views.ProductSearch.as_view(), name="search_results"),
    path('product/add/', views.ProductCreate.as_view(), name='product_add'),
    path('product/update/<int:id>/<slug:slug>/',
         views.ProductUpdate.as_view(),
         name='product_update'),
    path('product/delete/<int:id>/<slug:slug>/',
         views.ProductDelete.as_view(),
         name='product_delete'),
]
