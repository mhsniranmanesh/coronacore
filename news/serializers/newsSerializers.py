from rest_framework import serializers

from news.models.news import Feed


class GetAllFeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        exclude = ['details']


class GetFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
