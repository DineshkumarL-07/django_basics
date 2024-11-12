from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404
from customer.models import Customer
# Create your views here.

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    # return HttpResponse(customer)
    context = {
        'customer' : customer,
    }
    return render(request, 'customer_details.html', context)


    # try:
    #     customer = Customer.objects.get(pk=pk)
    #     print(customer)
    # except:
    #     raise Http404
    
