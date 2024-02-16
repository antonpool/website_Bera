
from .models import Articles, Category
from django.shortcuts import render
from django.views.generic import DetailView, ListView


def news(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/news_shop.html', {'news': news})


class PostListView(ListView):
    model = Category
    context_object_name = "post_list" #название в шаблоне
    template_name = "news/post_lis.html" #файл html шаблон

    def get_queryset(self):
        return Category.objects.filter(category__slug=self.kwargs.get("slug"))

class PostDetailViews(DetailView):
    model = Articles
    context_object_name = "post"
    template_name = "news/single-post.html"
    slug_url_kwarg = "post_slug"