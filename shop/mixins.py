from django.shortcuts import get_object_or_404

from .models import Product


class ProductMixin(object):
    model = Product

    def get_queryset(self):
        self.product = get_object_or_404(Product, id=self.kwargs['id'],
                                         slug=self.kwargs['slug'])
        return Product.objects.filter(id=self.product.id,
                                      slug=self.product.slug)