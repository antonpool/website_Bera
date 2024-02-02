from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {'title': 'Миленушка'})

def repair(request):
    data = {
        'title': 'Ремонт клюшек словарь'

    }
    return render(request, 'main/repair.html')

def shop(request):
    return render(request, 'main/shop.html')

def contact(request):
    return render(request, 'main/contact.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def reviews(request):
    return render(request, 'main/reviews.html')