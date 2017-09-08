from django.db.models import Q
from django.db import connection
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class GetUserInfoAPIView(APIView):
    """
    get free drivers by date range

    """

    def get(self, request, format=None, *args, **kwargs):
        '''
            Override default get
        '''
        username = self.request.GET.get("username")

        cursor = connection.cursor()

        cursor.execute('''SELECT id, username, is_superuser
                          FROM auth_user
                          WHERE username = %s
                       ''',[username])

        result = cursor.fetchall()

        free_drivers = []

        for i in result:
            free_driver = {}
            free_driver['id'] = i[0]
            free_driver['username'] = i[1]
            free_driver['is_superuser'] = i[2]
            free_drivers.append(free_driver)

        return Response(free_drivers)