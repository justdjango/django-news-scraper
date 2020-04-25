from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from django.shortcuts import reverse
from .models import NewsItem, ScrapeRecord
from .forms import ScrapeForm
from .tasks import scrape_async


class ScrapeRecordListView(generic.FormView):
    template_name = 'scrape_history.html'
    form_class = ScrapeForm

    def get_success_url(self):
        return reverse("scrape-history")

    def form_valid(self, form):
        scrape_async.delay()
        return super(ScrapeRecordListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ScrapeRecordListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        qs = ScrapeRecord.objects.all()
        paginator = Paginator(qs, 20)
        try:
            qs = paginator.page(page)
        except PageNotAnInteger:
            qs = paginator.page(1)
        except EmptyPage:
            qs = paginator.page(paginator.num_pages)
        context.update({
            "object_list": qs
        })
        return context


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
