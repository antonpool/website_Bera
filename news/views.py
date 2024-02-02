
from .models import Articles
from django.shortcuts import render


def news(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/news_shop.html', {'news': news})

