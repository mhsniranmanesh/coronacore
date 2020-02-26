from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from locations.models.userLocations import UserLocations
from locations.serializers.userLocationSerializers import UserUpdateLocationSerializer
from profiles.models.user import User


class UserUpdateLocationView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        serializer = UserUpdateLocationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = request.user
                longitude = serializer.validated_data.get('longitude')
                latitude = serializer.validated_data.get('latitude')
                location = Point(longitude, latitude)
                user.last_location = location
                user.save()
                UserLocations.objects.create(user=user, location=location)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)