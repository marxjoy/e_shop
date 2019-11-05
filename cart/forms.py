from django import forms


class CartAddProductForm(forms.Form):
    """
    Form supports adding product to Cart or
    updating quantity of product in Cart.
    """
    quantity = forms.IntegerField(min_value=1, max_value=1000000, initial=1)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)