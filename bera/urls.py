from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('gallery/', include('gallery.urls')),

    # path('repair', include('main.urls')),
    # path('shop', include('main.urls')),
    # path('delivery', include('main.urls')),
    # path('reviews', include('main.urls')),
    # path('contact', include('main.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

