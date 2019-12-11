from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('account.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
]

# only for debug mode. Images directory
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
