from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from news.constants.newsConstants import MAX_INITIAL_FEED_COUNT
from news.models.news import Feed
from news.serializers.newsSerializers import GetAllFeedsSerializer, GetFeedSerializer


class GetAllFeedsView(ListAPIView):
    queryset = Feed.objects.all().order_by('-date_created')[:MAX_INITIAL_FEED_COUNT]
    permission_classes = (IsAuthenticated,)
    serializer_class = GetAllFeedsSerializer


class GetFeedView(RetrieveAPIView):
    queryset = Feed.objects.all()
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated,)
    serializer_class = GetFeedSerializer

