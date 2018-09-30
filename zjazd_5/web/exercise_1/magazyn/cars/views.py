from django.shortcuts import render, HttpResponse

# Create your views here.
from cars.models import Car


def cars_list(request):
    car = Car.objects.all()
    return render(
        request=request,
        context={'cars': car},
        template_name='cars_list.html'

    )


def cars_details(request, id):
    car = Car.objects.get(pk=id)
    output = f"Car: {car.id} <br><br>"
    output += f"Marka: {car.marka} <br>"
    output += f"Model: {car.model_auta} <br>"
    output += f"Rok produkcji: {car.rok_produkcji} <br>"
    output += f"Typ nadwozia: {car.typ_nadwozia} <br>"
    output += f"http://127.0.0.1:8080/cars/{id}/fotka"
    return HttpResponse(output)

def cars_photo(request, id):
    car = Car.objects.get(pk=id)
    photo = car.fotka
    return HttpResponse(photo)
