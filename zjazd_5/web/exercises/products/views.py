from django.shortcuts import render, HttpResponse

# Create your views here.
from products.models import Products


def hello_world(request):
    return HttpResponse("Hello World")


def hello_world_name(request, name):
    return HttpResponse("Hello World " + name)


def product_list(request):
    products = Products.objects.all()

    return render(
        request=request,
        context={'products': products},
        template_name='products_list.html'
    )

    # output = ""
    # for product in products:
    #     output += f'{product.id} | <a href="/products/{product.id}">{product.name}</a><br>'
    # return HttpResponse(output)


def product_details(request, id):
    product = Products.objects.get(pk=id)
    output = f"Product: {product.id} <br><br>"
    output += f"Name: {product.name} <br>"
    output += f"Description: {product.description} <br>"
    output += f"Is available: {product.is_available} <br>"

    return HttpResponse(output)
