from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from connections.views.connectionsViews import ConnectionsAddContact, ConnectionsRequestConnection, \
    GetUserConnectionRequests, ConnectionsAcceptConnection


urlpatterns = {
    url(r'^contacts/add/$', ConnectionsAddContact.as_view(), name="add-contacts"),
    url(r'^request/send/$', ConnectionsRequestConnection.as_view(), name="request_connection"),
    url(r'^request/accept/$', ConnectionsAcceptConnection.as_view(), name="accept_request_connection"),
    url(r'^request/get/all/$', GetUserConnectionRequests.as_view(), name="get-all-request_connection"),
}
urlpatterns = format_suffix_patterns(urlpatterns)