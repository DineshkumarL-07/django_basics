from django.http import HttpResponse
from django.shortcuts import render
from customer.models import Customer

def home(request):

    customer = Customer.objects.all()
    context = {
        'customer' : customer,
    }
    return render(request, 'home.html', context)