
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    # path('1', views.bootstrap, name='bootstrap'),
    # path('2', views.b2, name='2'),
    path('<slug:slug>/', views.PostListView.as_view(), name = 'post_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailViews.as_view(), name = 'post_single')
]




