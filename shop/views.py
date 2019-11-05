from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from cart.forms import CartAddProductForm

from .mixins import ProductMixin
from .models import Product


class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 8
    template_name = 'shop/product/product_list.html'


class ProductDetail(ProductMixin, DetailView, FormMixin):
    context_object_name = 'product'
    template_name = 'shop/product/product_detail.html'
    form_class = CartAddProductForm


class ProductSearch(ListView):
    model = Product
    paginate_by = 8
    template_name = 'shop/product/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(
                   Q(name__icontains=query) |
                   Q(manufacturer__icontains=query))
        else:
            return Product.objects.all()


class ProductCreate(PermissionRequiredMixin, ProductMixin, CreateView):
    fields = ['name', 'manufacturer', 'description', 'price', 'image']
    template_name = 'shop/product/product_form.html'
    permission_required = 'shop.add_product'


class ProductUpdate(PermissionRequiredMixin, ProductMixin, UpdateView):
    fields = ['name', 'manufacturer', 'description', 'price', 'image']
    template_name = 'shop/product/product_form.html'
    permission_required = 'shop.change_product'


class ProductDelete(PermissionRequiredMixin, ProductMixin, DeleteView):
    success_url = reverse_lazy('shop:product_list')
    template_name = 'shop/product/product_confirm_delete.html'
    permission_required = 'shop.delete_product'
