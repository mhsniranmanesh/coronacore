from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from news.views.newsViews import GetAllFeedsView, GetFeedView

urlpatterns = {
    url(r'^feed/all/$', GetAllFeedsView.as_view(), name="get-all-feeds"),
    url(r'^feed/get/(?P<uuid>[0-9a-f-]+)/$', GetFeedView.as_view(), name="get-feed"),
}
urlpatterns = format_suffix_patterns(urlpatterns)