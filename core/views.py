from django.views import generic
from .models import NewsItem, ScrapeRecord
from .tasks import scrape_site_async


class ScrapeRecordListView(generic.ListView):
    template_name = 'scrape_history.html'
    paginate_by = 20
    model = ScrapeRecord


class NewsItemListView(generic.ListView):
    template_name = 'news_item_list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = NewsItem.objects.all()

        title = self.request.GET.get('title', None)
        if title:
            qs = qs.filter(title__icontains=title)

        return qs.order_by("-publish_date")

    def get_context_data(self, **kwargs):
        context = super(NewsItemListView, self).get_context_data(**kwargs)
        count = NewsItem.objects.all().count()
        context.update({
            "total_count": count
        })
        return context
