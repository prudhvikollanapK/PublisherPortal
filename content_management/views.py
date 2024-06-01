from django.shortcuts import render, redirect
from .models import ContentOffering, Transaction
from .forms import ContentOfferingForm
from django.shortcuts import get_object_or_404


def add_content_offering(request):
    if request.method == 'POST':
        form = ContentOfferingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContentOfferingForm()
    return render(request, 'content_management/add_content_offering.html', {'form': form})


def home(request):
    offerings = ContentOffering.objects.all()
    return render(request, 'content_management/home.html', {'offerings': offerings})


def add_to_cart(request, offering_id):
    offering = get_object_or_404(ContentOffering, id=offering_id)
    cart = request.session.get('cart', [])
    cart.append(offering.id)
    request.session['cart'] = cart
    return redirect('home')


def view_cart(request):
    cart = request.session.get('cart', [])
    offerings = ContentOffering.objects.filter(id__in=cart)
    total_price = sum(offering.price for offering in offerings)
    return render(request, 'content_management/cart.html', {'offerings': offerings, 'total_price': total_price})


def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        offerings = ContentOffering.objects.filter(id__in=cart)
        total_price = sum(offering.price for offering in offerings)
        transaction = Transaction.objects.create(total_price=total_price)
        transaction.content_offerings.set(offerings)
        request.session['cart'] = []
        return render(request, 'content_management/checkout_success.html')
    return redirect('view_cart')

