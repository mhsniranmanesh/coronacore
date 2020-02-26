from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from locations.views.userLocationViews import UserUpdateLocationView

urlpatterns = {
    url(r'^update/$', UserUpdateLocationView.as_view(), name="update-user-location"),
}
urlpatterns = format_suffix_patterns(urlpatterns)