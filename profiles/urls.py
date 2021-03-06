from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from profiles.views.userViews import UserCreateView, UserUpdateInfosView

urlpatterns = {
    url(r'^$', UserCreateView.as_view(), name="create-user"),
    url(r'^update-infos/$', UserUpdateInfosView.as_view(), name="update-profile-infos"),
}
urlpatterns = format_suffix_patterns(urlpatterns)