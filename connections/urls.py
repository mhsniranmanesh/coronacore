from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from connections.views.connectionsViews import ConnectionsAddContact

urlpatterns = {
    url(r'^contacts/add/$', ConnectionsAddContact.as_view(), name="add-contacts"),
}
urlpatterns = format_suffix_patterns(urlpatterns)