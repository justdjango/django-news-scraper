from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import NewsItemListView, ScrapeRecordListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsItemListView.as_view(), name='news-item-list'),
    path('history/', ScrapeRecordListView.as_view(), name='scrape-history')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
