from io import BytesIO
import json
import weasyprint

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from cart.cart import Cart

from .models import Order, OrderItem


@login_required
def order_create(request):
    cart = Cart(request)
    if len(cart) > 0:
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        order.save()
        cart.clear()

        # sending email
        subject = f"Confirmation of purchase. Order {order.id}"
        message = "Please find attached the invoice for purchase"
        email = EmailMessage(
            subject, message, 'e_mail@mail.com', [order.user.email])

        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out,
                                               stylesheets=stylesheets)
        email.attach(f"order_{order.id}.pdf",
                          out.getvalue(),
                          'application/pdf')
        email.send()

        return render(request,
                      'orders/order/created.html',
                      {'order': order})
    else:
        return redirect('shop:product_list')
